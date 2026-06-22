def inches_to_millimeters(inches):
    conversion_factor = {'in': 25.4}
    if 'in' not in conversion_factor:
        raise ValueError("Invalid unit. Use 'in'.")
    return inches * conversion_factor['in']
if __name__ == '__main__':
    print(inches_to_millimeters(1))
    print(inches_to_millimeters(10))