def find_the_middle_value_among_three_filter_valid(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    if a == b or b == c or a == c:
        return None
    
    sorted_values = sorted([a, b, c])
    return sorted_values[1]

if __name__ == '__main__':
    num1 = 10
    num2 = 5
    num3 = 15
    middle_value = find_the_middle_value_among_three_filter_valid(num1, num2, num3)
    print(middle_value)