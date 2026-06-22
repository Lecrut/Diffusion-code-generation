def generate_number_pyramid(height=5):
    result = []
    for i in range(1, height + 1):
        row_num = 0
        for j in range(1, i + 1):
            row_num += j
        row_str = " ".join(str(row_num) for _ in range(i))
        spaces = " " * (height - i)
        result.append(spaces + row_str)
    return result

if __name__ == '__main__':
    print(generate_number_pyramid())