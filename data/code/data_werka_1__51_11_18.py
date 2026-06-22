def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length_sample = 7.5
    width_sample = 3.2
    perimeter_result = calculate_perimeter(length_sample, width_sample)
    print(f"Perimeter of rectangle with length {length_sample} and width {width_sample}: {perimeter_result}")