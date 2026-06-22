def median_of_three(a, b, c):
    if not all(isinstance(i, (int, float)) for i in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    
    return b

if __name__ == '__main__':
    num1 = 5
    num2 = 3
    num3 = 8
    median_result = median_of_three(num1, num2, num3)
    print(median_result)