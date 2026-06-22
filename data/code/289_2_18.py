def validate_unit(unit):
    if unit != 'in':
        raise ValueError("Invalid unit. Use 'in'.")

def inches_to_millimeters(inches):
    validate_unit('in')
    return inches * 25.4
if __name__ == '__main__':
    print(inches_to_millimeters(1))
    print(inches_to_millimeters(0))
    try:
        print(inches_to_millimeters('a'))
    except ValueError as e:
        print(e)