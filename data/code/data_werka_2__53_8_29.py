def calculate_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    area = 25.0
    side_length = calculate_side_length(area)
    print(side_length)