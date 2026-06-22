def generate_pyramid(height=5):
    result = []
    for i in range(1, height + 1):
        row_nums = [str(j) for j in range(1, i + 1)]
        row_str = ' '.join(row_nums)
        padded_row = row_str.center(height * 2 - 1)
        result.append(padded_row)
    return result

if __name__ == '__main__':
    print('\n'.join(generate_pyramid()))