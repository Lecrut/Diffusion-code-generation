def _next_fib_pair(current_a, current_b):
    return current_b, current_a + current_b

def fibonacci_generator(limit_count):
    a = 0
    b = 1
    counter = 0
    while counter < limit_count:
        yield a
        a, b = _next_fib_pair(a, b)
        counter += 1

if __name__ == '__main__':
    sample_limit = 10
    collected_fib_sequence = list(fibonacci_generator(sample_limit))
    print(collected_fib_sequence)