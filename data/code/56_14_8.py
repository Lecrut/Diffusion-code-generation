def get_multiplication_table(value, limit=10):
    return [value * i for i in range(1, limit + 1)]

if __name__ == '__main__':
    result = get_multiplication_table(4)
    print(result)