def generate_hollow_square(side_length):
    if side_length < 1:
        return []
    if side_length == 1:
        return ["*"]
    
    border_row = "*" * side_length
    middle_row = "*" + " " * (side_length - 2) + "*"
    
    result = [border_row]
    for _ in range(side_length - 2):
        result.append(middle_row)
    result.append(border_row)
    
    return result

if __name__ == '__main__':
    sample_side = 7
    print("\n".join(generate_hollow_square(sample_side)))
    print("\n".join(generate_hollow_square(3)))
    print("\n".join(generate_hollow_square(5)))
    print("\n".join(generate_hollow_square(1)))