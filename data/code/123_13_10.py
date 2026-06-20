def sum_generator(n):
    return sum(i for i in range(1, n + 1))

if __name__ == '__main__':
    print(sum_generator(100))