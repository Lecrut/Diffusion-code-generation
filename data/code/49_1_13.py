def print_star_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    
    pattern = []
    for i in range(size):
        row = ''
        for j in range(size):
            if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                row += '*'
            else:
                row += ' '
        pattern.append(row)
    return pattern

if __name__ == '__main__':
    result = print_star_square(5)
    for line in result:
        print(line)