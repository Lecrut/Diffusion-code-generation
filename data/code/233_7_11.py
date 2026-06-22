def fill_rectangle(width, height):
    return ('*' * width + '\n') * height

if __name__ == '__main__':
    print(fill_rectangle(5, 3))