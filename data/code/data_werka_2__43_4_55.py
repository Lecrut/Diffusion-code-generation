def calculate_square_area(side_length: float) -> float:
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    
    def square(value: float) -> float:
        return value * value
    
    return square(side_length)

if __name__ == '__main__':
    sample_side_length = 4.5
    area = calculate_square_area(sample_side_length)
    print(area)