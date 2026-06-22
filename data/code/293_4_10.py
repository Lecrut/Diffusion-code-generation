conversion_factors = {
    's': 1,
    'm': 60,
    'h': 3600,
    'd': 86400,
    'w': 604800
}

def convert_time(value, from_unit, to_unit):
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid unit provided")
    return value * (conversion_factors[from_unit] / conversion_factors[to_unit])

if __name__ == '__main__':
    try:
        print(convert_time(1, 'h', 'm'))
        print(convert_time(24, 'd', 's'))
        print(convert_time(7, 'w', 'hours'))
    except ValueError as e:
        print(e)