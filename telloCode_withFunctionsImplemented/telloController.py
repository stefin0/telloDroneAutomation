"""
Avaliable functions:

	tello.Tello(str units) - creates tello object
		Arguments:
			str units: the units to use for all other functions: "cm" (default), "in", "m", "ft"

			
	takeoff() - the tello takes off
	land() - the tello lands
	
	
	move_forward(int distance) - the tello flys forward
	move_backward(int distance) - the tello flys backwards
	move_right(int distance) - the tello flys right
	move_left(int distance) - the tello flys left
	move_up(int distance) - the tello flys up
	move_down(int distance) - the tello flys down
	
		For all move_xx functions:
			Arguments:
				int distance: the distance to move:
					if units == "cm", 20 <= distance <= 500
					if units == "in", 8 <= distance <= 
					if units == "m", 
					if units == "ft", 

					
	flip(str direction) - the tello flips in the direction specified
		Arguments:
			str direction: the direction for the tello to flip: "l", "r", "f", "b", "lb", "lf", "rb" or "rf"
	
	
	rotate_cw(int degrees) - the tello rotates clockwise
	rotate_ccw(int degrees) - the tello rotates counter-clockwise
	
		For all rotate_xx functions:
			Arguments:
				int degrees: the number of degrees for the tello to rotate
	
	
	spin(str direction, int rotations) - the tello spins around fully
		Arguments:
			str direction: the direction to rotate "cw" or "ccw"
			int rotations: the number of full revolutions
			
			
	fly_poly(int sides, int distance) - the tello flies around the perimeter of a polygon
		Arguments:
			int sides: The number of sides of the polygon
			int distance: The length of each side of the polygon (Restricted by move())
	
	
	set_speed() - sets the speed the tello will move at
	
	
	get_battery() - returns the remaming battery percentage
	get_speed() - returns the speed of the tello (not the speed the tello is currently moving at, but the speed it is set to move at)
	get_flight_time() - returns the time that the tello has been in the air
"""
# CS4Me Project - Drone Competition and Hack-a-thon
# Jason Eissayou, Alonso Rios, 
# Stefin Racho, Victoria Zepeda, Sherly Yaghoubi
import tello
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(message)s')
log = logging.getLogger('Drone app')
log.info('Starting')

t = tello.Tello()
try:
	start_battery = t.get_battery()
	print("Battery percentage: %s" % start_battery)

	# Starts the takeoff
	t.takeoff()

	# Waits half a second for input
	time.sleep(1.5)

	# Adjust height down 12in (30.5cm)
	t.move_down(30.5)

	# Waits half a second
	time.sleep(0.5)

	# Moves forward 23in (58.4cm)
	# Taking off and aligning
	t.move_forward(58.4)
	
	# Waits half a second
	time.sleep(0.5)

	# Rotates clockwise 90 degrees
	t.rotate_cw(90)

	# Waits half a second
	time.sleep(0.5)

	# Moves forward 140in (355.6cm)
	# Moving through the first obstacle
	t.move_forward(358.1)

	# Waits half a second
	time.sleep(0.5)

	# Rotate counter-clockwise 90 degrees
	# Lines up drone for next obstacle
	t.rotate_cw(270)

	# Waits half a second
	time.sleep(0.5)

	# Finished Obstacle 1, Time to go through obstacle 2

	# Move forward 74in (188cm)
	# Moves through the second obstacle
	t.move_forward(188)

	# Waits half a second
	time.sleep(0.5)

	# Rotate counter-clockwise 90 degrees
	# Line up with Hospital landing pad
	t.rotate_cw(320)

	# Move foward 37in (94 cm)
	# Land and Finish the sequence!
	t.move_forward(77)



except Exception as e:
	log.error(e)
t.land()
end_battery = t.get_battery()
print("Battery percentage: %s" % end_battery)
print("Battery used for flight %s" % (start_battery - end_battery))