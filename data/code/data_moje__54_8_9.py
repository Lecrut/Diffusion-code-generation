def print_hollow_square(size):
    lines = [
        "".join(
            '*' if i == 0 or i == size - 1 or j == 0 or j == size - 1 else ' '
            for j in range(size)
        )
        for i in range(size)
    ]
    print("\n".join(lines))

if __name__ == '__main__':
    print_hollow_square(7)