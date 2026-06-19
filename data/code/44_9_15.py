def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length_sample = 15.0
    width_sample = 7.5
    perimeter_result = calculate_perimeter(length_sample, width_sample)
    print(f"Length: {length_sample}")
    print(f"Width: {width_sample}")
    print(f"Perimeter: {perimeter_result}")