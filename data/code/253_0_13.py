def find_the_middle_value_among_three_transform(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers.")
    
    sorted_values = sorted([a, b, c])
    return sorted_values[1]

if __name__ == '__main__':
    print(find_the_middle_value_among_three_transform(5, 3, 9))