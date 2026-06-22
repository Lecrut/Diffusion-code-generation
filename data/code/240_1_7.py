def compute_area(side_length: int) -> int:
    area = side_length * side_length
    return area

if __name__ == '__main__':
    sample_side = 8
    computed_area = compute_area(sample_side)
    print(f"The area of a square with side {sample_side} is: {computed_area}")