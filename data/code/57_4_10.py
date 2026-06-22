def get_fibonacci_list(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

if __name__ == '__main__':
    result = get_fibonacci_list(200)
    print(result)