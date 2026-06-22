def generate_hollow_square(size: int) -> str:
    if size <= 0:
        return ""
    
    if size == 1:
        return "*"
    
    rows = []
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    
    rows.append(top_bottom)
    for _ in range(size - 2):
        rows.append(middle)
    rows.append(top_bottom)
    
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5))