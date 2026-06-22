def build_number_pyramid(height):
    result = []
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        line = f"{spaces}{numbers}"
        result.append(line)
    return '\n'.join(result)

if __name__ == '__main__':
    print(build_number_pyramid(7))