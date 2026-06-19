import math

def compare_temperatures(temp1, temp2):
    if math.isclose(temp1, temp2, rel_tol=1e-09, abs_tol=0.0):
        return 'equal'
    elif temp1 < temp2:
        return 'less than'
    else:
        return 'greater than'
if __name__ == '__main__':
    temp1 = 36.6000000001
    temp2 = 36.6
    result = compare_temperatures(temp1, temp2)
    print(result)