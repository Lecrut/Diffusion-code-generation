def generate_rectangle(width, height):
    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    rectangle = generate_rectangle(5, 3)
    for row in rectangle:
        print(row)