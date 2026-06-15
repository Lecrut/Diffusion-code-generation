def print_star_pattern(n):
    for i in range(n):
        print('*' * (2 * i + 1))
if __name__ == '__main__':
    print_star_pattern(5)
    print("-" * 10)
    print_star_pattern(3)