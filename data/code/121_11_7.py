def compare_large_integers(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
if __name__ == '__main__':
    result = compare_large_integers(12345678901234567890, 98765432109876543210)
    print(result)