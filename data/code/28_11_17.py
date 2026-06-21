def sort_descending(num1, num2):
    if num1 > num2:
        return num1, num2
    return num2, num1

if __name__ == '__main__':
    a = 42
    b = 17
    result = sort_descending(a, b)
    print(result)