import time

input_time = int(input('Enter seconds: '))

for x in reversed(range(input_time)):
    seconds = x % 60 
    minutes = int(x/60) % 60
    hours = int(x/3600) 
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print('Timer is up')

