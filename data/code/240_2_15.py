def validate_side_length(side_length):
    if not isinstance(side_length, (int, float)) or side_length <= 0:
        raise ValueError("Side length must be a positive number")

def calculate_area(side_length):
    validate_side_length(side_length)
    return side_length * side_length

if __name__ == '__main__':
    sample_side = 10
    area = calculate_area(sample_side)
    print(area)