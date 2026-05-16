import math
def max_difference(A, B):
    min_a = min(A)
    max_a = max(A)
    min_b = min(B)
    max_b = max(B)
    diff1 = abs(max_a - min_b)
    diff2 = abs(min_a - max_b)
    diff3 = abs(max_a - max_b)
    diff4 = abs(min_a - min_b)
    return max(diff1, diff2, diff3, diff4)
if __name__ == '__main__':
    A_sample = [1, 5, 10]
    B_sample = [3, 7, 12]
    result = max_difference(A_sample, B_sample)
    print(result)