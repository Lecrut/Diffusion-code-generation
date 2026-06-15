if __name__ == '__main__':
    width = 10
    height = 5
    box_chars = "#"
    for y in range(height):
        line = ""
        for x in range(width):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                line += box_chars
            else:
                line += " "
        print(line)