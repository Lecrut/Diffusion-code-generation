def generate_left_aligned_pyramid():
    return ["".join(str(num) for num in range(1, row + 1)) for row in range(1, 7)]

if __name__ == '__main__':
    result = generate_left_aligned_pyramid()
    for line in result:
        print(line)