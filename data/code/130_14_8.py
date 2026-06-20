def is_zero(num):
    return num == 0

if __name__ == '__main__':
    value = -123.456
    result = is_zero(value)
    print(result)
    value = 0.0
    result = is_zero(value)
    print(result)