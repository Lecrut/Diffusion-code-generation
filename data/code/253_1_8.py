def find_the_middle_value_among_three_validate(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    numbers = [a, b, c]
    numbers.sort()
    
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    num1 = 8
    num2 = 3
    num3 = 6
    middle_value = find_the_middle_value_among_three_validate(num1, num2, num3)
    print(middle_value)