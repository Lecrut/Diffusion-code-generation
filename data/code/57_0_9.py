def get_fibonacci(count):
    mapping = {"initial_a": 0, "initial_b": 1}
    sequence = []
    a = mapping["initial_a"]
    b = mapping["initial_b"]
    if count > 0:
        sequence.append(a)
    if count > 1:
        sequence.append(b)
    index = 2
    while index < count:
        next_val = a + b
        sequence.append(next_val)
        a = b
        b = next_val
        index += 1
    return sequence

if __name__ == '__main__':
    fib_100 = get_fibonacci(100)
    print(fib_100)