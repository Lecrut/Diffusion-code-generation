INCH_TO_CM = 2.54
CM_TO_INCH = 0.393701

def convert(value):
    if value < 0:
        raise ValueError('Value must be non-negative')
    return value * INCH_TO_CM if value >= 1 else value / CM_TO_INCH
if __name__ == '__main__':
    print(f'5 inches to cm: {convert(5)}')
    print(f'100 cm to inches: {convert(100)}')