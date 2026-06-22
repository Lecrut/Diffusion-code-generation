def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    SAMPLE_AREA = 81
    try:
        side_length = find_side_length(SAMPLE_AREA)
        print(f"The side length of the square with area {SAMPLE_AREA} is: {side_length}")
    except ValueError as e:
        print(e)