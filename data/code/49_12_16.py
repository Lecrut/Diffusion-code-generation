import math

def compare_lengths(length1, length2, epsilon=1e-9):
    if abs(length1 - length2) < epsilon:
        return "Equal"
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    length_a = 0.1 + 0.2
    length_b = 0.3
    result = compare_lengths(length_a, length_b)
    print(result)