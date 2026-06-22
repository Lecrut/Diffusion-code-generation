def generate_hollow_square(side_length):
    if side_length <= 0:
        return ""
    if side_length == 1:
        return "X"
    
    first_row = "X" * side_length
    middle_row = "X" + " " * (side_length - 2) + "X"
    last_row = first_row
    
    if side_length == 2:
        return first_row + "\n" + last_row
    
    lines = [first_row]
    for _ in range(side_length - 2):
        lines.append(middle_row)
    lines.append(last_row)
    
    return "\n".join(lines)

if __name__ == "__main__":
    side = 5
    result = generate_hollow_square(side)
    print(result)