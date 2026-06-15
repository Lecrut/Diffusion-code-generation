def print_star_pyramid(n):
    if n == 0:
        return
    print_star_pyramid(n - 1)
    if n > 0:
        print(" " * (n - 1) + "*")
if __name__ == '__main__':
    print_star_pyramid(5)