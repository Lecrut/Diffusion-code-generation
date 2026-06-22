def build_number_pyramid(levels=4):
    result = []
    for level in range(1, levels + 1):
        row = list(range(1, level + 1))
        result.append(row)
    return result

if __name__ == '__main__':
    pyramid = build_number_pyramid()
    for level in pyramid:
        print(' '.join(str(num) for num in level))