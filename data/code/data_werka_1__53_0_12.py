def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    SAMPLE_VALUES = [1, 2.5, 3.75, 0, -2]
    for value in SAMPLE_VALUES:
        try:
            area = calculate_square_area(value)
            print(f"The area of a square with side length {value} is {area}.")
        except ValueError as e:
            print(e)