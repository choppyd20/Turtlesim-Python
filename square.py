#!/usr/bin/env python
import rospy
import numpy
from geometry_msgs.msg import Twist

rospy.init_node('square', anonymous=True)
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(10) # 10hz

print('Starting square . . .')

# TODO: Modify the code below so that the robot moves in a square

while not rospy.is_shutdown():
    twist = Twist()

    twist.linear.x = 0.5
    twist.angular.z = 0.5

    pub.publish(twist)
    rate.sleep() #sleep until the next time to publish

