def get_diamond_line(index, total_height):
    space_count = abs(total_height // 2 - index)
    star_count = total_height - 2 * space_count
    spaces = ' ' * space_count
    stars = '*' * star_count
    return spaces + stars + spaces

def generate_diamond(n):
    result = []
    for i in range(n):
        result.append(get_diamond_line(i, n))
    for i in range(n - 2, -1, -1):
        result.append(get_diamond_line(i, n))
    return result

if __name__ == '__main__':
    lines = generate_diamond(8)
    for line in lines:
        print(line)