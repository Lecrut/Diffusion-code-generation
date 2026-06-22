def build_symmetric_number_pyramid(rows=6):
    result = []
    max_width = 2 * rows - 1
    for i in range(rows):
        num = i + 1
        num_str = str(num)
        count = 2 * i + 1
        sequence = [num_str for _ in range(count)]
        line_content = ''.join(sequence)
        padding = (max_width - len(line_content)) // 2
        line = ' ' * padding + line_content + ' ' * padding
        result.append(line)
    return result

if __name__ == '__main__':
    pyramid = build_symmetric_number_pyramid(6)
    print('\n'.join(pyramid))