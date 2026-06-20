def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    num = 25
    result = is_odd(num)
    print(result)