def yards_to_kilometers(yards):
    if not isinstance(yards, (int, float)):
        raise ValueError("Input must be a number")
    return yards * 0.0254 * 3.28084

if __name__ == '__main__':
    sample_values = [10, 20.5, 0.0, -5]
    for value in sample_values:
        try:
            result = yards_to_kilometers(value)
            print(f"{value} yards is {result} kilometers")
        except ValueError as e:
            print(e)