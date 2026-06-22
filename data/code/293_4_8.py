CONVERSION_FACTORS = {
    's': 1,
    'm': 60,
    'h': 3600,
    'd': 86400,
    'w': 604800
}

def time_converter(value, from_unit, to_unit):
    return value * CONVERSION_FACTORS[from_unit] / CONVERSION_FACTORS[to_unit]

if __name__ == '__main__':
    print(time_converter(1, 'h', 'm'))
    print(time_converter(24, 'd', 's'))
    print(time_converter(7, 'w', 'hours'))