def generate_number_pyramid():
    levels = 4
    pyramid = []
    for level in range(1, levels + 1):
        current_level_numbers = list(range(1, 2 ** level))
        pyramid.append(current_level_numbers)
    return pyramid
if __name__ == '__main__':
    result = generate_number_pyramid()
    for level in result:
        print(' '.join(map(str, level)))