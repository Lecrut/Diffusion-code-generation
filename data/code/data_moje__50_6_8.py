MAX_HEIGHT = 6

def print_symmetric_triangle(height: int) -> None:
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(f"{spaces}{stars}")
    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(f"{spaces}{stars}")

if __name__ == '__main__':
    print_symmetric_triangle(MAX_HEIGHT)