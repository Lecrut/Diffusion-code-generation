def find_the_middle_value_among_three_compare(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers")
    
    return sorted([a, b])[1]

if __name__ == '__main__':
    result = find_the_middle_value_among_three_compare(5, 3)
    print(result)