def calculate_perimeter(length, width):
    return 2 * (length + width)

def process_rectangles(rectangles):
    results = []
    for rect in rectangles:
        length, width = rect
        if length > 0 and width > 0:
            perimeter = calculate_perimeter(length, width)
            results.append(perimeter)
        else:
            results.append("Invalid input: Length and width must be positive numbers.")
    return results

if __name__ == '__main__':
    rectangles = [(7, 3), (5, 2), (-1, 4), (8, 0)]
    for result in process_rectangles(rectangles):
        print(result)