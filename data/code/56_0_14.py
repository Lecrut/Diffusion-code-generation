def multiplication_table(n):
    return [[n * col for col in range(1, 11)] for row in range(1, 11)]

if __name__ == '__main__':
    result = multiplication_table(5)
    print(result)