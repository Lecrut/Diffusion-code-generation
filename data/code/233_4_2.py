def create_rectangle(symbol, width, height):
    rectangle = ""
    for _ in range(height):
        rectangle += symbol * width + "\n"
    return rectangle.rstrip('\n')
if __name__ == '__main__':
    print(create_rectangle("X", 5, 3))
    print("\n" + create_rectangle("#", 10, 2))