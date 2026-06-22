def print_star_pattern(size):
    line = "*" * size
    for _ in range(size):
        print(line)

if __name__ == "__main__":
    print_star_pattern(6)