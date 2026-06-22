def create_hollow_square(side_length, char):
    if side_length == 0:
        return ""
    if side_length == 1:
        return char
    top_bottom = char * side_length
    middle = char + " " * (side_length - 2) + char
    rows = [top_bottom]
    for _ in range(side_length - 2):
        rows.append(middle)
    rows.append(top_bottom)
    return "\n".join(rows)

if __name__ == '__main__':
    side = 5
    symbol = 'X'
    result = create_hollow_square(side, symbol)
    print(result)