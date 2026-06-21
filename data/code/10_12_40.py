import math

def compare_temperatures(temp1, temp2):
    tolerance = 1e-09
    if math.isclose(temp1, temp2, abs_tol=tolerance):
        return 'equal'
    elif temp1 < temp2:
        return 'less than'
    else:
        return 'greater than'
if __name__ == '__main__':
    temperature1 = 36.600000001
    temperature2 = 36.6
    relationship = compare_temperatures(temperature1, temperature2)
    print(relationship)