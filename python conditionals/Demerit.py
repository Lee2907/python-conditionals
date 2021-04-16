speed = int(input("enter speed: "))
avg = int(input("average speed: "))

points = (speed - avg)/5

if speed < 60:
    print("OK")

elif speed== 60:
    print("OK")

if points < 12:
    print("demerit: "+ str(points))

else:
    print("time to go to jail")


