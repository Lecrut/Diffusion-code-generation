area_of_square = lambda side_length: side_length ** 2

if __name__ == '__main__':
    sample_values = {'side1': 3, 'side2': 4, 'side3': 5}
    for name, length in sample_values.items():
        print(f"Area of square with {name} side {length}: {area_of_square(length)}")