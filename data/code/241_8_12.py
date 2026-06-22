def calculate_area(length: int, width: int) -> int:
    return length * width

if __name__ == '__main__':
    length = 6
    width = 8
    area = calculate_area(length, width)
    print(f"Area of {length} and {width}: {area}")