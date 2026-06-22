def generate_pyramid():
    lines = ['1', '1 2 1', '1 2 3 2 1']
    return '\n'.join(lines)

if __name__ == '__main__':
    print(generate_pyramid())