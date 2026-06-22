def generate_left_aligned_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        row = ' '.join(str(j) for j in range(1, i + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    pyramid = generate_left_aligned_pyramid(6)
    for line in pyramid:
        print(line)