def cubic_meters_to_cubic_feet(m3):
    if not isinstance(m3, (int, float)):
        raise ValueError("Input must be a number")
    return m3 * 35.3146667

if __name__ == '__main__':
    sample_values = [1, 2.5, 10]
    for value in sample_values:
        result = cubic_meters_to_cubic_feet(value)
        print(f"{value} cubic meters is {result} cubic feet")