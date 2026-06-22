def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    
    edge_row = "*" * n
    middle_row = "*" + " " * (n - 2) + "*"
    
    top_and_bottom = [edge_row]
    middle = [middle_row] * (n - 2)
    
    result = top_and_bottom + middle + top_and_bottom
    return result

if __name__ == '__main__':
    size = 5
    pattern = generate_hollow_square(size)
    for row in pattern:
        print(row)