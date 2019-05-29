#!/bin/bash 
PIES="rpi01 rpi02 rpi03 rpi04 rpi05 rpi06 rpi07 rpi08 rpi09 rpi10 rpi11 rpi12 rpi13 rpi14 rpi15 rpi16 rpi17 rpi18 rpi19 rpi20 rpi21"

for i in $PIES ; do 

	ping $i -c 1 -W 1 &>/dev/null
	if [ $? -eq 0 ] ; then
		echo [$i] PIE ALIVE
	else
		echo [$i] PIE DEAD
	fi
done	
