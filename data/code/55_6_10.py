def generate_hollow_alphabet_triangle(base_width):
    result = []
    if base_width < 1:
        return result
    
    for row in range(1, base_width + 1):
        spaces_before = base_width - row
        line = " " * spaces_before
        
        if row == 1:
            line += "A"
        elif row == base_width:
            line += "A"
            if row > 1:
                line += " " * ((row - 1) * 2 - 1)
            line += "A"
        else:
            line += "A"
            line += " " * ((row - 1) * 2 - 1)
            line += chr(64 + row)
        
        result.append(line)
    
    return "\n".join(result)

if __name__ == '__main__':
    sample_base = 6
    print(generate_hollow_alphabet_triangle(sample_base))