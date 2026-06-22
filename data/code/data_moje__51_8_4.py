def print_number_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        line = ''
        for j in range(i):
            line += str(i)
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(print_number_pyramid(5))