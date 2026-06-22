import sys

def validate_temperature(temp):
    try:
        float(temp)
    except ValueError as e:
        print(f'Invalid temperature value: {e}', file=sys.stderr)
        raise ValueError from e

def compare_temperatures(temp1, temp2):
    validate_temperature(temp1)
    validate_temperature(temp2)
    
    epsilon = 1e-09
    if abs(float(temp1) - float(temp2)) < epsilon:
        return 'equal'
    elif float(temp1) < float(temp2):
        return 'less than'
    else:
        return 'greater than'

if __name__ == '__main__':
    temperature1 = 40.6000000005
    temperature2 = 40.6
    relationship = compare_temperatures(temperature1, temperature2)
    print(relationship)