def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_list = [0, 1]
    i = 2
    while i < n:
        next_val = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_val)
        i += 1
    return fib_list

if __name__ == '__main__':
    print(generate_fibonacci(20))