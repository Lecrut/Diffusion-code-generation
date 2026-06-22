def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    
    square = [top_bottom]
    for _ in range(n - 2):
        square.append(middle)
    square.append(top_bottom)
    
    return "\n".join(square)

if __name__ == '__main__':
    n = 5
    print(generate_hollow_square(n))