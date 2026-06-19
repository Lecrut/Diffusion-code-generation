import math

def compare_lengths(length1, length2, epsilon=1e-9):
    if math.isclose(length1, length2, abs_tol=epsilon):
        return None
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    length_a = 3.141592653589793
    length_b = 3.141592653589794
    result = compare_lengths(length_a, length_b)
    print(result)