def validate_inputs(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("All inputs must be numbers")
    
def sort_descending(a, b, c):
    validate_inputs(a, b, c)
    return tuple(sorted([a, b, c], reverse=True))

if __name__ == '__main__':
    result = sort_descending(3.5, 1, 2.7)
    print(result)