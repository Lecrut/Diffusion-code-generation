def generate_sequence():
    return (3 * n - 2 for n in range(1, 11))

if __name__ == '__main__':
    print(list(generate_sequence()))