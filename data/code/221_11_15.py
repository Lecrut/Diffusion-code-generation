def validate_inputs(a, b, c):
    if not all(isinstance(i, int) for i in [a, b, c]):
        raise ValueError("All inputs must be integers")
    return a, b, c

def sort_three_numbers(a, b, c):
    a, b, c = validate_inputs(a, b, c)
    
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    return (a, b, c)

if __name__ == '__main__':
    result = sort_three_numbers(5, 3, 1)
    print(result)