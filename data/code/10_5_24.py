def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f'T1 is warmer by {difference} degrees'
    elif temp2 > temp1:
        yield f'T2 is warmer by {difference} degrees'
    else:
        yield 'Both temperatures are equal'

if __name__ == '__main__':
    t1 = 30
    t2 = 25
    for result in compare_temperatures(t1, t2):
        print(result)