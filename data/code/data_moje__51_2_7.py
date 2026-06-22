def generate_left_aligned_pyramid():
    result = []
    for row in range(1, 7):
        numbers = [str(num) for num in range(1, row + 1)]
        result.append(" ".join(numbers))
    return result

if __name__ == '__main__':
    pyramid_lines = generate_left_aligned_pyramid()
    print(pyramid_lines)