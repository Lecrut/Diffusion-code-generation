import math

def compare_lengths(length1, length2, epsilon=1e-09):
    if abs(length1 - length2) < epsilon:
        return None
    elif length1 > length2:
        return length1
    else:
        return length2
if __name__ == '__main__':
    sample_length1 = 1.000000001
    sample_length2 = 1.000000002
    result = compare_lengths(sample_length1, sample_length2)
    print(result)