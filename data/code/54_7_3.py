def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    
    top_bottom = "*" + " " * (n - 2) + "*"
    middle = "*" + " " * (n - 2) + "*"
    
    rows = []
    rows.append(top_bottom)
    for _ in range(n - 2):
        rows.append(middle)
    if n > 1:
        rows.append(top_bottom)
    
    return rows

if __name__ == '__main__':
    size = 5
    result = generate_hollow_square(size)
    for line in result:
        print(line)