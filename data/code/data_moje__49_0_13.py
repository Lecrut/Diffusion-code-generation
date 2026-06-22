def generate_square_pattern(side_length):
    result = []
    for i in range(side_length):
        row = '*' * side_length
        result.append(row)
    return result

if __name__ == '__main__':
    pattern = generate_square_pattern(5)
    for line in pattern:
        print(line)