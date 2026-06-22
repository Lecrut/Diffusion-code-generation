def calculate_perimeter(sides):
    if not all((isinstance(side, (int, float)) and side >= 0 for side in sides)):
        raise ValueError('All sides must be non-negative numbers')
    return sum(sides)
if __name__ == '__main__':
    try:
        print(calculate_perimeter([3, 4, 5]))
        print(calculate_perimeter([0, 0, 0]))
        print(calculate_perimeter([1.5, 2.5, 3.5]))
        print(calculate_perimeter([10, 20]))
    except ValueError as e:
        print(e)