def generate_hollow_triangle():
    rows = 8
    result = []
    for i in range(1, rows + 1):
        if i == 1:
            result.append('*')
        elif i == rows:
            result.append('*' * (2 * i - 1))
        else:
            stars = '*' + ' ' * (2 * i - 3) + '*'
            result.append(stars)
    return result

if __name__ == '__main__':
    output = generate_hollow_triangle()
    for line in output:
        print(line)