if __name__ == '__main__':
    a, b, c = 3, 1, 2
    sorted_sequence = sorted([a, b, c], key=lambda x: x)
    print(*sorted_sequence)