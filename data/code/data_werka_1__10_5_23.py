def temperature_comparison(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f'T1 is warmer by {difference} degrees'
    elif temp2 > temp1:
        yield f'T2 is warmer by {difference} degrees'
    else:
        yield 'Both temperatures are equal'

if __name__ == '__main__':
    for result in temperature_comparison(30, 25):
        print(result)