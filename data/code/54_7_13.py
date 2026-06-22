def generate_hollow_square(size: int) -> list[str]:
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    
    full_row = "*" * size
    inner_count = size - 2
    middle_row = "*" + " " * inner_count + "*"
    
    if size == 2:
        return [full_row, full_row]
    
    result = [full_row]
    for _ in range(inner_count):
        result.append(middle_row)
    result.append(full_row)
    return result

if __name__ == '__main__':
    sample_size = 5
    square_pattern = generate_hollow_square(sample_size)
    for row in square_pattern:
        print(row)