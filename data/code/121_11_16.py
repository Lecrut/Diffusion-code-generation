def compare_large_integers(a, b):
    size_a = len(a)
    size_b = len(b)
    if size_a > size_b:
        return 1
    elif size_b > size_a:
        return -1
    else:
        for i in range(size_a):
            if a[i] > b[i]:
                return 1
            elif b[i] > a[i]:
                return -1
        return 0
if __name__ == '__main__':
    num1 = [9, 8, 7]
    num2 = [6, 5, 4, 3]
    result1 = compare_large_integers(num1, num2)
    print(result1)
    num3 = [10, 20]
    num4 = [10, 20]
    result2 = compare_large_integers(num3, num4)
    print(result2)