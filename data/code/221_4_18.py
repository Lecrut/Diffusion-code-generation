def sort_three_numbers(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    return a, b, c

if __name__ == '__main__':
    print(sort_three_numbers(3.14, 2.71, 1.61))