def compare_temperatures(temp1, temp2):
    difference = abs(temp1 - temp2)
    if temp1 > temp2:
        yield f'T1 is warmer by {difference} degrees'
    elif temp2 > temp1:
        yield f'T2 is warmer by {difference} degrees'
    else:
        yield 'Both temperatures are equal'

if __name__ == '__main__':
    sample_values = [(30, 25), (20, 20), (15, 20)]
    for t1, t2 in sample_values:
        for result in compare_temperatures(t1, t2):
            print(result)