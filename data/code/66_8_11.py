def convert_kilometers_to_meters(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number")
    if kilometers < 0:
        raise ValueError("Input must be a non-negative number")
    return kilometers * 1000

if __name__ == '__main__':
    sample_values = [5, 10.5, 0]
    for value in sample_values:
        result = convert_kilometers_to_meters(value)
        print(f"{value} km is {result} m")