def sum_of_areas(side1, side2):
    if not (isinstance(side1, (int, float)) and isinstance(side2, (int, float))):
        raise ValueError("Both sides must be numbers")
    
    return 2 * (side1 ** 2 + side2 ** 2)

if __name__ == '__main__':
    result = sum_of_areas(3, 4)
    print(result)