def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {
        'small': 3,
        'medium': 5.5,
        'large': 10
    }
    for label, value in sample_values.items():
        print(f"{label}: {calculate_square_area(value)}")