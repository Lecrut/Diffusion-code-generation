COUNT_LIMIT = 10

def fib_sequence():
    current = 0
    next_val = 1
    generated = 0
    while generated < COUNT_LIMIT:
        yield current
        current, next_val = next_val, current + next_val
        generated += 1

if __name__ == '__main__':
    print(list(fib_sequence()))