def calculate_perimeter(num_sides, side_length):
    if num_sides < 3:
        raise ValueError("Number of sides must be at least 3")
    return num_sides * side_length

if __name__ == '__main__':
    try:
        perimeter = calculate_perimeter(5, 3)
        print(f"Perimeter: {perimeter}")
    except ValueError as e:
        print(e)