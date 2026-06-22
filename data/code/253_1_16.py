def find_the_middle_value_among_three_validate(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    values = sorted([a, b, c])
    middle_value = values[1]
    return middle_value

if __name__ == '__main__':
    num1 = 8
    num2 = 4
    num3 = 6
    result = find_the_middle_value_among_three_validate(num1, num2, num3)
    print(result)