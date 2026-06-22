def print_hollow_square(side_length, char):
    if side_length == 0:
        return ""
    if side_length == 1:
        return char
    full_row = char * side_length
    middle_row = char + " " * (side_length - 2) + char
    result = [full_row]
    for _ in range(side_length - 2):
        result.append(middle_row)
    result.append(full_row)
    return "\n".join(result)

if __name__ == '__main__':
    side = 5
    symbol = 'X'
    print(print_hollow_square(side, symbol))