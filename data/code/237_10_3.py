if __name__ == '__main__':
    fib_cache = {0: 0, 1: 1}
    
    def fibonacci(n):
        if n in fib_cache:
            return fib_cache[n]
        fib_cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return fib_cache[n]
    
    sequence = [fibonacci(i) for i in range(20)]
    print(sequence)