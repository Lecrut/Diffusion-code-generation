def compare_temperatures(temp1, temp2):
    epsilon = 1e-09
    if abs(temp1 - temp2) < epsilon:
        return 'equal'
    elif temp1 < temp2:
        return 'less than'
    else:
        return 'greater than'
if __name__ == '__main__':
    temperature1 = 36.6000000001
    temperature2 = 36.6
    result = compare_temperatures(temperature1, temperature2)
    print(result)