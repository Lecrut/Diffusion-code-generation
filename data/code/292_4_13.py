def calculate_perimeter(num_sides, side_length):
    return num_sides * side_length

if __name__ == '__main__':
    polygon_data = {
        "sides": 5,
        "length": 3
    }
    perimeter = calculate_perimeter(polygon_data["sides"], polygon_data["length"])
    print(f"Number of sides: {polygon_data['sides']}")
    print(f"Side length: {polygon_data['length']}")
    print(f"Perimeter: {perimeter}")