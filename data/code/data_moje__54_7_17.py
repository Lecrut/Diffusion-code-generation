def generate_hollow_square(side_length):
    if side_length <= 0:
        return ""
    if side_length == 1:
        return "*"
    
    top_bottom_row = "*" * side_length
    middle_row = "*" + " " * (side_length - 2) + "*"
    
    lines = [top_bottom_row]
    for _ in range(side_length - 2):
        lines.append(middle_row)
    lines.append(top_bottom_row)
    
    return "\n".join(lines)

if __name__ == '__main__':
    sample_side = 5
    result = generate_hollow_square(sample_side)
    print(result)
    
    sample_small = 1
    result_small = generate_hollow_square(sample_small)
    print(result_small)
    
    sample_large = 8
    result_large = generate_hollow_square(sample_large)
    print(result_large)