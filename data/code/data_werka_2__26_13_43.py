def is_greater_than(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both arguments must be integers.")
    return a > b

if __name__ == '__main__':
    try:
        result1 = is_greater_than(25, 20)
        print(result1)
        
        result2 = is_greater_than(10, 30)
        print(result2)
        
        result3 = is_greater_than(15, 15)
        print(result3)
    except ValueError as e:
        print(e)