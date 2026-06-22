fib = [0, 1] + [fib[i-1] + fib[i-2] for i in range(2, 15)]
if __name__ == '__main__':
    print(fib)