def calculate_perimeter(sides):
    if not all((isinstance(side, (int, float)) for side in sides)):
        raise ValueError('All sides must be numeric')
    if any((side < 0 for side in sides)):
        raise ValueError('Sides must be non-negative')
    return sum(sides)
if __name__ == '__main__':
    try:
        print(calculate_perimeter([3, 4, 5]))
        print(calculate_perimeter([2, 2, 2, 2]))
        print(calculate_perimeter([1.5, 2.5, 3.5]))
        print(calculate_perimeter([-1, 2, 3]))
    except ValueError as e:
        print(e)