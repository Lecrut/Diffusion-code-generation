def generate_left_aligned_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        result.append(' '.join(str(i) * i))
    return result

if __name__ == '__main__':
    print(generate_left_aligned_pyramid())