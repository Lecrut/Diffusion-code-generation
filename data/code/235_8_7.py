def generate_arrowhead(n):
    if n % 2 == 0:
        raise ValueError("Width must be odd")
    
    arrow = ""
    for i in range(1, n + 1):
        arrow += " " * (n - i) + "*" * (i + 2 * (i - 1)) + "\n"
    
    return arrow

if __name__ == '__main__':
    width = 5
    output = generate_arrowhead(width)
    print(output.rstrip())