import time
import sys


print('Let''s start countdown')
print(' ')
print('Instructions: 1)Input time to countdown from.')
print(' ')
temp=0
c=':'
try:
    hours=int(input('Enter Hours: '))
    mins=int(input('Enter Minutes: '))
    secs=int(input('Enter Seconds: '))
    print(' ')
    while hours > -1:
        while mins > -1:
            while secs > 0:
                secs=secs-1
                time.sleep(1)
                sec1 = ('%02.f' % secs)  
                min1 = ('%02.f' % mins)
                hour1 = ('%02.f' % hours)
                sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))
            mins=mins-1
            secs=60
        hours=hours-1
        mins=59
        print("")
        print('Countdown Complete.')
        time.sleep(5)
except:
    print("numbers only")
    print("")

