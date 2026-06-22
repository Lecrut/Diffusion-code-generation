def draw_diamond(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        bars = '|' * (2 * i + 1)
        print(spaces + bars)

if __name__ == '__main__':
    draw_diamond(5)