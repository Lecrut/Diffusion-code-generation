def generate_hollow_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        if i == 1:
            line = ' ' * (rows - i) + '*'
        elif i == rows:
            line = ' ' * (rows - i) + '*' + '  ' * (i - 1) + '*'
        else:
            inner_spaces = '  ' * (i - 2)
            line = ' ' * (rows - i) + '*' + inner_spaces + '  ' + '*'
        result.append(line)
    return result

if __name__ == '__main__':
    sample_rows = 5
    output = generate_hollow_pyramid(sample_rows)
    for line in output:
        print(line)