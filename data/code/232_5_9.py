def print_growing_sequence():
    sequence = {i: i for i in range(100)}
    i = 0
    while i <= 99:
        print(sequence[i])
        i += 1

if __name__ == '__main__':
    print_growing_sequence()