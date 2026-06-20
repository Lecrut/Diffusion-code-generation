def is_odd(n):
    return n & 1 == 1

if __name__ == '__main__':
    sample_value = 9
    result = is_odd(sample_value)
    print(result)