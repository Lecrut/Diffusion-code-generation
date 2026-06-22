def calculate_area(base, height):
    if base <= 0 or height <= 0:
        return 0
    return base * height

if __name__ == '__main__':
    sample_base = 6.5
    sample_height = 4.3
    result = calculate_area(sample_base, sample_height)
    print(result)