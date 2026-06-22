def is_float(value):
    return isinstance(value, float)

def are_close(a, b, tol):
    return abs(a - b) < tol

def compare_lengths(length1, length2, epsilon=1e-09):
    if not (is_float(length1) and is_float(length2)):
        raise ValueError('Both lengths must be floating-point numbers.')
    
    if are_close(length1, length2, epsilon):
        return None
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    length_a = 3.141592653589793
    length_b = 3.141592653589795
    result = compare_lengths(length_a, length_b)
    print(result)