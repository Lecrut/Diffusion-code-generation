def max_difference(A, B):
    min_A = min(A)
    max_A = max(A)
    min_B = min(B)
    max_B = max(B)
    diff1 = abs(max_A - min_B)
    diff2 = abs(min_A - max_B)
    diff3 = abs(max_A - max_B)
    diff4 = abs(min_A - min_B)
    return max(diff1, diff2, diff3, diff4)
if __name__ == '__main__':
    A = [1, 5, 10]
    B = [3, 7, 12]
    result = max_difference(A, B)
    print(result)