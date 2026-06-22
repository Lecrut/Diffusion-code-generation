def sort_three_numbers(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All inputs must be integers")
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    return a, b, c

if __name__ == '__main__':
    print(sort_three_numbers(3, 1, 2))