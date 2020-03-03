# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import string
import random
import time
import threading


class Subpub(Node):

    def __init__(self):
        super().__init__('B')
        self.publisher_ = self.create_publisher(String, 'A', 10)
        self.length = 10
        self.subscription = self.create_subscription(
            String,
            'B',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        msg = String()
        msg.data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.length))
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    ps = Subpub()
    rclpy.spin(ps)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
