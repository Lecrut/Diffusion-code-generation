def find_the_middle_value_among_three_validate(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("All inputs must be numbers")
    
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_validate(5, 3, 8))