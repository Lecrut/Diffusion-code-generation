def render_diamond(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    lines = []
    half_n = (n + 1) // 2
    
    for i in range(half_n):
        line = ' ' * (half_n - i - 1) + '*' * (2 * i + 1)
        lines.append(line)
        if i < half_n - 1:
            lines.insert(0, line)
    
    for line in lines:
        print(line)

if __name__ == '__main__':
    render_diamond(5)