def square_area(side_length: float) -> float:
    return side_length * side_length

if __name__ == '__main__':
    sample_sides = [5.0, 3.5, 10.123456789]
    for side in sample_sides:
        print(square_area(side))