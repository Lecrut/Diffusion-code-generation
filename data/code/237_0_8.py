if __name__ == '__main__':
    fib_dict = {0: 0, 1: 1}
    n = 10
    for i in range(2, n):
        fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
    print(list(fib_dict.values()))