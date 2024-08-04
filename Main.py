import time

timerDuration = int(input("Set your duration in seconds unit!\n-> "))
hours, minutes, seconds,  = 0, 0, 0

for i in range(timerDuration):
	print(100 * '\n')

	seconds += 1
	if seconds == 60:
		minutes += 1
		seconds = 0
	elif minutes == 60:
		hours += 1
		minutes = 0

	print(f"{hours}h : {minutes}m : {seconds}s")
	time.sleep(1)