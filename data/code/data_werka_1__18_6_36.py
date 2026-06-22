def compare_large_integers(num1, num2):
    return num1 > num2

if __name__ == '__main__':
    large_num1 = 10**100 + 42
    large_num2 = 10**100 + 41
    result = compare_large_integers(large_num1, large_num2)
    print(result)