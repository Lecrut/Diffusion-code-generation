def number_pyramid_generator(row_count):
    for row in range(1, row_count + 1):
        numbers = " ".join(str(x) for x in range(1, row + 1))
        total_width = (row_count * 2) - 1
        padding = " " * ((total_width - (row * 2 - 1) + 1) // 2)
        yield padding + numbers

if __name__ == '__main__':
    for line in number_pyramid_generator(8):
        print(line)