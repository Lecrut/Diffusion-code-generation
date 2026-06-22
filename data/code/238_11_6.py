def create_hollow_square(side_length):
    if side_length < 2:
        return ""
    
    square = []
    for i in range(side_length):
        if i == 0 or i == side_length - 1:
            row = "*" * side_length
        else:
            row = "*" + " " * (side_length - 2) + "*"
        square.append(row)
    
    return "\n".join(square)

if __name__ == '__main__':
    print(create_hollow_square(4))