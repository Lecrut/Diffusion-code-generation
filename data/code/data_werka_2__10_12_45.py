def compare_temperatures(temp1, temp2):
    precision = 1e-09
    if abs(temp1 - temp2) < precision:
        return 'equal'
    elif temp1 < temp2:
        return 'less than'
    else:
        return 'greater than'

if __name__ == '__main__':
    temperature_values = {
        'temp1': 40.6000000005,
        'temp2': 40.6
    }
    relationship = compare_temperatures(temperature_values['temp1'], temperature_values['temp2'])
    print(relationship)