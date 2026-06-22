def generate_pyramid():
    lines = []
    levels = 4
    for level in range(1, levels + 1):
        number_of_items = 2 ** level - 1
        numbers = list(range(1, number_of_items + 1))
        line_items = []
        for i in range(number_of_items):
            line_items.append(str(numbers[i]))
        line = ' '.join(line_items)
        lines.append(line)
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid())