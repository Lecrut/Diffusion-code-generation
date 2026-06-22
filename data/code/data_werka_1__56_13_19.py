def calculate_area(length):
    return length * length

def calculate_perimeter(length):
    return 4 * length

if __name__ == '__main__':
    side_length = 5
    rectangle_area = calculate_area(side_length)
    rectangle_perimeter = calculate_perimeter(side_length)
    square_area = calculate_area(side_length)
    square_perimeter = calculate_perimeter(side_length)

    comparison_results = {
        'rectangle': {
            'area': rectangle_area,
            'perimeter': rectangle_perimeter
        },
        'square': {
            'area': square_area,
            'perimeter': square_perimeter
        }
    }

    print(comparison_results)