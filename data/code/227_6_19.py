def print_star_pyramid(n):
    if n <= 0:
        raise ValueError("Height must be greater than 0")
    
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))

if __name__ == '__main__':
    try:
        print_star_pyramid(3)
    except ValueError as e:
        print(e)