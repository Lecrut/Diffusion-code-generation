def print_star_pyramid(n):
    if n == 0:
        return
    for i in range(1, n + 1):
        print("*" * (2 * i - 1))
if __name__ == '__main__':
    print_star_pyramid(5)