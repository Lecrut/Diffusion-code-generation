def generate_sequence():
    current = 1
    for _ in range(5):
        print(current)
        current *= 2

if __name__ == '__main__':
    generate_sequence()