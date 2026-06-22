def calculate_area(length: int, width: int) -> int:
    return length * width

if __name__ == '__main__':
    length1 = 6
    width1 = 8
    area1 = calculate_area(length1, width1)
    print(f"Area of {length1} and {width1}: {area1}")

    length2 = 9
    width2 = 3
    area2 = calculate_area(length2, width2)
    print(f"Area of {length2} and {width2}: {area2}")