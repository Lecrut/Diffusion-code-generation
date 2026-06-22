def generate_number_pyramid(height):
    if height <= 0:
        return []
    
    rows = []
    center_offset = height - 1
    
    for row in range(1, height + 1):
        number = row
        spaces = " " * (center_offset - row + 1)
        numbers = " ".join(str(i) for i in range(1, row + 1))
        reverse_numbers = " ".join(str(i) for i in range(row - 1, 0, -1))
        
        if reverse_numbers:
            line_content = f"{numbers} {reverse_numbers}"
        else:
            line_content = f"{numbers}"
            
        line = f"{spaces}{line_content}"
        rows.append(line)
        
    return rows

if __name__ == '__main__':
    result = generate_number_pyramid(5)
    for row in result:
        print(row)