def generate_hollow_square(side_length):
    if side_length < 2:
        return ""
    
    square = []
    for i in range(side_length):
        row = ["*"] * side_length
        if i > 0 and i < side_length - 1:
            for j in range(1, side_length - 1):
                row[j] = " "
        square.append("".join(row))
    
    return "\n".join(square)

if __name__ == '__main__':
    sample_output = generate_hollow_square(5)
    print(sample_output)