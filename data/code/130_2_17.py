def is_number(value):
    return isinstance(value, (int, float))

def is_zero(value):
    if not is_number(value):
        raise ValueError("Input must be an int or float")
    
    zero_epsilon = 1e-9
    return value == 0 or (isinstance(value, float) and abs(value) < zero_epsilon)

if __name__ == '__main__':
    print(is_zero(0))
    print(is_zero(0.0))
    print(is_zero(-0))
    print(is_zero(-0.0))
    try:
        print(is_zero("1"))
    except ValueError as e:
        print(e)