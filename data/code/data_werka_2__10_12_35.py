import sys

def compare_temperatures(temp1, temp2):
    try:
        float(temp1)
        float(temp2)
    except ValueError as e:
        print(f'Invalid input: {e}', file=sys.stderr)
        return None
    epsilon = 1e-09
    if abs(temp1 - temp2) < epsilon:
        return 'equal'
    elif temp1 < temp2:
        return 'less than'
    else:
        return 'greater than'
if __name__ == '__main__':
    temperature1 = 38.4000000003
    temperature2 = 38.4
    relationship = compare_temperatures(temperature1, temperature2)
    if relationship is not None:
        print(relationship)