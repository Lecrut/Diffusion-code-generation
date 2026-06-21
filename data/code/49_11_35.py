import math

def compare_lengths(length1, length2, epsilon=1e-9):
    if abs(length1 - length2) < epsilon:
        return "Equal"
    elif length1 > length2:
        return length1
    else:
        return length2

if __name__ == '__main__':
    sample_length1 = 3.141592653589793
    sample_length2 = 3.141592653589794
    result = compare_lengths(sample_length1, sample_length2)
    print(result)