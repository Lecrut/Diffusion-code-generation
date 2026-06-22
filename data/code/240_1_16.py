def compute_area(side_length: int) -> int:
    return side_length * side_length

if __name__ == '__main__':
    side1 = 5
    area1 = compute_area(side1)
    print(f"The area of a square with side {side1} is: {area1}")