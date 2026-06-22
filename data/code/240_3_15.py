def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive numeric value")

def calculate_area(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_side_length = 5
    validate_side_length(sample_side_length)
    area = calculate_area(sample_side_length)
    print(area)