def generate_right_aligned_pyramid():
    rows = 8
    max_width = rows * 2 - 1
    for i in range(1, rows + 1):
        num_count = i
        padding_count = max_width - num_count
        leading_spaces = ' ' * (max_width - num_count)
        line = leading_spaces + ''.join(str(j) for j in range(1, num_count + 1))
        yield line

if __name__ == '__main__':
    pyramid_generator = generate_right_aligned_pyramid()
    for chunk in pyramid_generator:
        print(chunk)