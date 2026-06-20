def calculate_rectangle_area(length, width):
    if not isinstance(length, (int, float)):
        raise TypeError('Length must be a number.')
    if not isinstance(width, (int, float)):
        raise TypeError('Width must be a number.')
    if length < 0:
        raise ValueError('Length must be non-negative.')
    if width < 0:
        raise ValueError('Width must be non-negative.')
    return length * width

def main():
    sample_lengths = [5, 10, 0, -5, 7.5]
    sample_widths = [3, 2, 4, 2, 3.0]
    results = []
    for length, width in zip(sample_lengths, sample_widths):
        try:
            area = calculate_rectangle_area(length, width)
            results.append(f'Length: {length}, Width: {width} -> Area: {area}')
        except (ValueError, TypeError) as e:
            results.append(f'Length: {length}, Width: {width} -> Error: {str(e)}')
    for result in results:
        print(result)
if __name__ == '__main__':
    main()