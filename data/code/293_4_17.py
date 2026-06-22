CONVERSION_FACTORS = {
    's': 1,
    'm': 60,
    'h': 3600,
    'd': 86400,
    'w': 604800
}

def convert_time(value, from_unit, to_unit):
    return value * CONVERSION_FACTORS[from_unit] / CONVERSION_FACTORS[to_unit]

if __name__ == '__main__':
    print(convert_time(1, 'hours', 'minutes'))
    print(convert_time(24, 'days', 'seconds'))
    print(convert_time(7, 'weeks', 'hours'))