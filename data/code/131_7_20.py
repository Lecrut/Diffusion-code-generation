def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    num1 = 48
    num2 = 18
    result = gcd_euclidean(num1, num2)
    print(result)