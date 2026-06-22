def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "*"
    
    top_bottom = "*" * n
    if n == 2:
        return f"{top_bottom}\n{top_bottom}"
    
    middle_row = "*" + " " * (n - 2) + "*"
    middle_rows = (middle_row + "\n") * (n - 2)
    
    return f"{top_bottom}\n{middle_rows}{top_bottom}"

if __name__ == '__main__':
    print(generate_hollow_square(5))