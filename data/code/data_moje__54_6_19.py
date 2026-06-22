def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    
    top_bottom = "*" * n
    middle = "*" + " " * (n - 2) + "*"
    
    result = [top_bottom] + [middle] * (n - 2) + [top_bottom]
    return result

if __name__ == '__main__':
    size = 5
    output = generate_hollow_square(size)
    for row in output:
        print(row)