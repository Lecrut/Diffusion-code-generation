def is_odd(n):
    return n & 1 != 0

if __name__ == '__main__':
    num = 9
    result = is_odd(num)
    print(result)