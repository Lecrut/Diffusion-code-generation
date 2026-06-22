def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be an integer or float.")
    if side_length <= 0:
        raise ValueError("Side length must be positive.")

def get_side_length_and_area(side_length):
    validate_side_length(side_length)
    area = side_length * side_length
    return (side_length, area)

if __name__ == '__main__':
    sample_values = [3, 7.5, 10]
    for value in sample_values:
        result = get_side_length_and_area(value)
        print(result)