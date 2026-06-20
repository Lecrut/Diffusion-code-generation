def multiply_decimals(a, b):
    return (a * 10**15) * (b * 10**15) // (10**30)

if __name__ == '__main__':
    result = multiply_decimals(0.1, 0.2)
    print(result)