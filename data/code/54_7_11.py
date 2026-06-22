def generate_hollow_square(size: int) -> list[str]:
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    if size == 2:
        return ["**", "**"]
    
    full_row = "*" * size
    middle_row = "*" + " " * (size - 2) + "*"
    
    result = [full_row]
    for _ in range(size - 2):
        result.append(middle_row)
    result.append(full_row)
    
    return result

if __name__ == '__main__':
    sample_size = 5
    output = generate_hollow_square(sample_size)
    for line in output:
        print(line)