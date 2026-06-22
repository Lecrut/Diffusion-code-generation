def median_of_three(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    return sorted([a, b, c])[1]

if __name__ == '__main__':
    num1 = 5
    num2 = 2
    num3 = 8
    median_result = median_of_three(num1, num2, num3)
    print(median_result)