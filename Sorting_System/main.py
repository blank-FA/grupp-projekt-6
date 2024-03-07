#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()

# Define motor ports
MOTOR_TOWER = Port.A
MOTOR_ARM = Port.B
MOTOR_CLAW = Port.C

# Define sensor ports
SENSOR_COLOR = Port.S1
SENSOR_TOUCH = Port.S2

# Define colors
COLOR_NONE = Color.NONE
COLOR_RED = Color.RED
COLOR_BLUE = Color.BLUE
COLOR_GREEN = Color.GREEN

# Define positions
POSITION_PICKUP = 0
POSITION_DROP_OFF = 90

# Define motor speeds
MOTOR_SPEED = 50

# Create motor objects
motor_tower = Motor(MOTOR_TOWER)
motor_arm = Motor(MOTOR_ARM)
motor_claw = Motor(MOTOR_CLAW)

# Create sensor objects
sensor_color = ColorSensor(SENSOR_COLOR)
sensor_touch = TouchSensor(SENSOR_TOUCH)

# Functions to control motors
def turn_tower(degrees):
    motor_tower.run_target(MOTOR_SPEED, degrees)

def move_arm(degrees):
    motor_arm.run_target(MOTOR_SPEED, degrees)

def control_claw(action):
    if action == 'open':
        motor_claw.run_target(MOTOR_SPEED, 90)
    elif action == 'close':
        motor_claw.run_target(-MOTOR_SPEED, 90)

# Function to check item presence
def check_item_presence():
    return sensor_color.color() != COLOR_NONE

# Function to get item color
def get_item_color():
    return sensor_color.color()

# Function to drop items off at different locations based on color
def drop_off_item(color):
    if color == COLOR_RED:
        turn_tower(POSITION_DROP_OFF_RED)
    elif color == COLOR_BLUE:
        turn_tower(POSITION_DROP_OFF_BLUE)
    elif color == COLOR_GREEN:
        turn_tower(POSITION_DROP_OFF_GREEN)
    move_arm(POSITION_DROP_OFF)
    control_claw('open')
    wait(1000)
    control_claw('close')

# Main functionality
def main():
    # Write your program here.
    ev3.speaker.beep()
    while True:
        if check_item_presence():
            item_color = get_item_color()
            if item_color != COLOR_NONE:
                move_arm(POSITION_PICKUP)
                control_claw('open')
                wait(1000)
                control_claw('close')
                move_arm(-POSITION_PICKUP)
                drop_off_item(item_color)
            else:
                print("No item detected!")
        else:
            print("No item detected!")
        wait(1000)

if __name__ == "__main__":
    main()
