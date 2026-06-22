def get_side_length_and_area(side_length):
    if side_length <= 0:
        raise ValueError('Side length must be positive')
    area = side_length * side_length
    return (side_length, area)

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 5,
        'large': 7.5
    }
    for label, value in sample_values.items():
        try:
            result = get_side_length_and_area(value)
            print(f"{label.capitalize()} - Side Length: {result[0]}, Area: {result[1]}")
        except ValueError as e:
            print(e)