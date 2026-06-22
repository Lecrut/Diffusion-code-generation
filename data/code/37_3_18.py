def calculate_parallelogram_area(base, height):
    if base <= 0 or height <= 0:
        return 0.0
    return float(base * height)

def get_test_parameters():
    return 12.5, 8.0

if __name__ == '__main__':
    b, h = get_test_parameters()
    result = calculate_parallelogram_area(b, h)
    print(result)