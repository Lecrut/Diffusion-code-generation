import math

def compare_temperatures(temp1, temp2):
    epsilon = 1e-09
    if math.isclose(temp1, temp2, rel_tol=epsilon):
        return 'equal'
    elif temp1 < temp2:
        return 'less than'
    else:
        return 'greater than'
if __name__ == '__main__':
    temperature1 = 98.600000001
    temperature2 = 98.6
    result = compare_temperatures(temperature1, temperature2)
    print(result)