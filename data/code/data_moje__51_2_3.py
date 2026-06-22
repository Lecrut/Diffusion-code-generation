def generate_left_aligned_pyramid(rows):
    return [str(i) for i in range(1, rows + 1)]

if __name__ == '__main__':
    result = generate_left_aligned_pyramid(6)
    print(result)