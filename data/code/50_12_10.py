def generate_hollow_triangle(size):
    if size < 1:
        return []
    result = []
    for i in range(1, size + 1):
        if i == size:
            result.append('* ' * i)
        elif i == 1:
            result.append('*')
        else:
            spaces = ' ' * (2 * (i - 1) - 1)
            result.append(f'*{spaces}*')
    return '\n'.join(result)

if __name__ == '__main__':
    print(generate_hollow_triangle(5))