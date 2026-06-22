def print_sequence():
    current = 0
    step = 1
    for _ in range(5):
        print(current)
        current += step
        step += 1

if __name__ == '__main__':
    print_sequence()