def render_diamond(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    pattern = [
        "   *",
        "  ***",
        " *****",
        "*******",
        " *****",
        "  ***",
        "   *"
    ]
    
    for line in pattern[:n]:
        print(line)
    for line in reversed(pattern[:-1]):
        print(line)

if __name__ == '__main__':
    render_diamond(7)