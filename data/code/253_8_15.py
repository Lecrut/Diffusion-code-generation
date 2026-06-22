def find_the_middle_value_among_three_compare(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers.")
    
    return sorted([a, b])[1]

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare(5, 3)
    print(result)