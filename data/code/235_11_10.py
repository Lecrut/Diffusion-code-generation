def render_diamond(n):
    if n < 1:
        raise ValueError("Diamond size must be at least 1")
    
    top_half = []
    for i in range(n):
        line = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        top_half.append(line)
    
    bottom_half = top_half[:n-1][::-1]
    diamond = top_half + bottom_half
    
    for line in diamond:
        print(line)

if __name__ == '__main__':
    render_diamond(5)