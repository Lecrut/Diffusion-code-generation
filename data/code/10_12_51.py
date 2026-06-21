import math

def compare_temperatures(temp1, temp2):
    try:
        float_temp1 = float(temp1)
        float_temp2 = float(temp2)
    except ValueError as e:
        raise ValueError(f'Invalid input: {e}') from e

    epsilon = 1e-09
    if math.isclose(float_temp1, float_temp2, abs_tol=epsilon):
        return 'equal'
    elif float_temp1 < float_temp2:
        return 'less than'
    else:
        return 'greater than'

if __name__ == '__main__':
    temperature1 = 36.7000000005
    temperature2 = 36.7
    try:
        relationship = compare_temperatures(temperature1, temperature2)
        print(relationship)
    except ValueError as e:
        print(e)