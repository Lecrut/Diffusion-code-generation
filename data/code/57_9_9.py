def get_fibonacci():
    fib = [0, 1]
    for _ in range(73):
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == '__main__':
    result = get_fibonacci()
    print(result)