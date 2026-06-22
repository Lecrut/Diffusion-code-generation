def generate_hollow_square(size: int) -> str:
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    
    top_bottom = "*" * size
    middle_inner = " " * (size - 2)
    middle_row = f"*{middle_inner}*"
    
    if size == 2:
        return f"{top_bottom}\n{top_bottom}"
    
    rows = [top_bottom]
    for _ in range(size - 2):
        rows.append(middle_row)
    rows.append(top_bottom)
    
    return "\n".join(rows)

if __name__ == "__main__":
    sample_size = 5
    result = generate_hollow_square(sample_size)
    print(result)