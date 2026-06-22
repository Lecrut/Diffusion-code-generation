def create_rectangle_pattern(width, height):
    pattern = ""
    for y in range(height):
        for x in range(width):
            digit = (x + y) % 10
            pattern += str(digit)
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(create_rectangle_pattern(5, 3))