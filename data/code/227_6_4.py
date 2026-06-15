def print_star_pyramid(n):
    if n == 0:
        return
    print_star_pyramid(n - 1)
    spaces = " " * (n - 1)
    print("*" * (2 * n - 1))
    print_star_pyramid(n - 1)
if __name__ == '__main__':
    num = 5
    print_star_pyramid(num)