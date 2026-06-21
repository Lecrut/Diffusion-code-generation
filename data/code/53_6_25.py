def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    SAMPLE_AREA = 36
    side_length = find_side_length(SAMPLE_AREA)
    print(f"The side length of a square with area {SAMPLE_AREA} is {side_length}")