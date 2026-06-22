def multiplication_table(n):
    return [[n * i for i in range(1, 11)] for j in range(1, 11)]

if __name__ == '__main__':
    result = multiplication_table(5)
    print(result)