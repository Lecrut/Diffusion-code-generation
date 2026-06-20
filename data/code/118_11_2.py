def multiply_large_integers(a, b):
    result = 0
    for i in range(len(b)):
        digit = int(b[len(b) - 1 - i])
        temp = a * (10 ** i)
        for j in range(digit):
            result += temp
    return result

if __name__ == '__main__':
    print(multiply_large_integers(123456789, 987654321))