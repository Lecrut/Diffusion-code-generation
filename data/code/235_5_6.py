MAX_VALUE = 5

def generate_triangle_pattern():
    pattern = []
    for i in range(1, MAX_VALUE + 1):
        spaces = ' ' * (MAX_VALUE - i)
        numbers = ''.join(str(j) for j in range(1, i + 1))
        pattern.append(spaces + numbers)
    return '\n'.join(pattern)

if __name__ == '__main__':
    print(generate_triangle_pattern())