def generate_left_aligned_pyramid():
    rows = 6
    result = []
    for i in range(1, rows + 1):
        line = ' '.join(str(j) for j in range(1, i + 1))
        result.append(line)
    return result

if __name__ == '__main__':
    pyramid = generate_left_aligned_pyramid()
    for line in pyramid:
        print(line)