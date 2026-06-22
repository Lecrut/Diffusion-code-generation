def construct_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    line_top_bottom = '*' * size
    line_middle = '*' + ' ' * (size - 2) + '*'
    result = [line_top_bottom]
    for _ in range(size - 2):
        result.append(line_middle)
    result.append(line_top_bottom)
    return result

if __name__ == '__main__':
    sample_size = 10
    square_lines = construct_hollow_square(sample_size)
    for line in square_lines:
        print(line)