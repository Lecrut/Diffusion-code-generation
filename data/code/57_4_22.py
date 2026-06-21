def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    sample_base = 7.0
    sample_height = 4.5
    area_result = calculate_parallelogram_area(sample_base, sample_height)
    print(f"The area of the parallelogram with base {sample_base} and height {sample_height} is: {area_result}")