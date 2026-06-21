def cubic_meters_to_cubic_feet(cubic_meters):
    if not isinstance(cubic_meters, (int, float)):
        raise ValueError('Input must be a number')
    conversion_factor = 35.3146667
    return cubic_meters * conversion_factor
if __name__ == '__main__':
    sample_values = [1, 2.5, 10, 0, -1]
    for value in sample_values:
        try:
            result = cubic_meters_to_cubic_feet(value)
            print(f'{value} cubic meters is {result} cubic feet')
        except ValueError as e:
            print(e)