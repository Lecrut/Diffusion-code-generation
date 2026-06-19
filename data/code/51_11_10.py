RECTANGLE_SIDES_COUNT = 2

def calculate_perimeter(length, width):
    return (length + width) * RECTANGLE_SIDES_COUNT

if __name__ == '__main__':
    sample_length_1 = 3
    sample_width_1 = 4
    print(f"Perimeter of rectangle with length {sample_length_1} and width {sample_width_1}: {calculate_perimeter(sample_length_1, sample_width_1)}")
    
    sample_length_2 = 5.5
    sample_width_2 = 2.3
    print(f"Perimeter of rectangle with length {sample_length_2} and width {sample_width_2}: {calculate_perimeter(sample_length_2, sample_width_2)}")