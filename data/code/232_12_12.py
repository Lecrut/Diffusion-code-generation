def print_incrementing_sequence(start=1, steps=5):
    current = start
    step_size = 1
    for _ in range(steps):
        print(current)
        current += step_size
        step_size += 1

if __name__ == '__main__':
    print_incrementing_sequence(2, 5)