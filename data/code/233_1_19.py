def generate_rectangle(width, height, symbol):
    return [symbol * width for _ in range(height)]

if __name__ == '__main__':
    rectangle = generate_rectangle(4, 6, '#')
    for row in rectangle:
        print(row)