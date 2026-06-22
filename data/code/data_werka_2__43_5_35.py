def compute_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    sample_values = {'side1': 3, 'side2': 4, 'side3': 5}
    for key, value in sample_values.items():
        print(f"Area of square with {key} length {value}: {compute_area(value)}")