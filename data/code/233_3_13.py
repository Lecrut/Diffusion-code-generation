def create_rectangle_pattern(width, height):
    digits = "0123456789"
    pattern = ""
    for y in range(height):
        for x in range(width):
            pattern += digits[(x + y) % len(digits)]
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(create_rectangle_pattern(10, 5))