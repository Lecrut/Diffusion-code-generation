def generate_hollow_square(side_length):
    if side_length <= 0:
        return ""
    if side_length == 1:
        return "X"
    
    top_bottom = "X" * side_length
    middle_rows = ["X" + " " * (side_length - 2) + "X"] * (side_length - 2)
    
    result_parts = [top_bottom]
    result_parts.extend(middle_rows)
    result_parts.append(top_bottom)
    
    return "\n".join(result_parts)

if __name__ == '__main__':
    side = 5
    square_output = generate_hollow_square(side)
    print(square_output)