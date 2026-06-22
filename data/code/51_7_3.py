def generate_right_aligned_pyramid():
    for i in range(1, 9):
        row_content = ' '.join(str(j) for j in range(1, i + 1))
        padding = ' ' * (8 - i) * 2
        yield f'{padding}{row_content}'

if __name__ == '__main__':
    for chunk in generate_right_aligned_pyramid():
        print(chunk)