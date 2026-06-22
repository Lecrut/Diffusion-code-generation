def swap(x, y):
    return y, x

def validate_input(a, b, c):
    if not all(isinstance(n, int) for n in (a, b, c)):
        raise ValueError("All inputs must be integers")

def sort_three_numbers(a, b, c):
    validate_input(a, b, c)
    
    if a > b:
        a, b = swap(a, b)
    if b > c:
        b, c = swap(b, c)
    if a > b:
        a, b = swap(a, b)
    
    return a, b, c

if __name__ == '__main__':
    print(sort_three_numbers(3, 1, 2))