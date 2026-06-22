import math

def compare_lengths(length1, length2, epsilon=1e-9):
    if math.isclose(length1, length2, rel_tol=epsilon):
        return "Equal"
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    length_a = 0.3333333333333333
    length_b = 1/3
    result = compare_lengths(length_a, length_b)
    print(result)