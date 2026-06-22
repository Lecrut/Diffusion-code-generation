def render_diamond(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    lines = []
    for i in range(n):
        line = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        lines.append(line)
    for i in range(n-2, -1, -1):
        lines.append(lines[i])
    
    for line in lines:
        print(line)

if __name__ == '__main__':
    diamond_size = 7
    render_diamond(diamond_size)