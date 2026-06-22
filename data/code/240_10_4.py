def calculate_square_area(side_length):
    return side_length * side_length
if __name__ == '__main__':
    sample_side = 7.2
    try:
        input_side = float(sample_side)
        if input_side < 0:
            raise ValueError('Side length cannot be negative.')
        area = calculate_square_area(input_side)
        print(f'The side length entered is: {input_side}')
        print(f'The area of the square is: {area:.2f}')
    except ValueError as e:
        print(f'Error: Invalid input. {e}')