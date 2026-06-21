import math

def compare_lengths(length1, length2, epsilon=1e-09):
    if not (isinstance(length1, float) and isinstance(length2, float)):
        raise ValueError('Both lengths must be floating-point numbers.')
    diff = abs(length1 - length2)
    if diff < epsilon:
        return None
    elif length1 > length2:
        return length1
    else:
        return length2
if __name__ == '__main__':
    length_a = 10.000000005
    length_b = 10.000000001
    result = compare_lengths(length_a, length_b)
    print(result)