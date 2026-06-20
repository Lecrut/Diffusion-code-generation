def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

if __name__ == '__main__':
    num1 = 48
    num2 = 18
    result = gcd(num1, num2)
    print(result)