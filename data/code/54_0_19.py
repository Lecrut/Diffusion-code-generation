def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    
    top_and_bottom = "*" * size
    middle_row = "*" + " " * (size - 2) + "*"
    
    rows = []
    rows.append(top_and_bottom)
    for _ in range(size - 2):
        rows.append(middle_row)
    if size > 1:
        rows.append(top_and_bottom)
    
    return "\n".join(rows)

if __name__ == '__main__':
    print(generate_hollow_square(5))