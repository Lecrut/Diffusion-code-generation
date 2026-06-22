def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def sort_three_bitwise(a, b, c):
    if not (is_number(a) and is_number(b) and is_number(c)):
        raise TypeError("All inputs must be numbers.")
    
    a, b = min(a, b), max(a, b)
    b, c = min(b, c), max(b, c)
    a, b = min(a, b), max(a, b)
    
    return a, b, c

if __name__ == '__main__':
    print(f"Sorting (1, 5, 3): {sort_three_bitwise(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {sort_three_bitwise(10, -2, 7)}")
    try:
        print(f"Sorting ('a', 5, 3): {sort_three_bitwise('a', 5, 3)}")
    except TypeError as e:
        print(f"Error caught: {e}")