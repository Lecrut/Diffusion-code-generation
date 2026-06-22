def generate_symmetric_pyramid(rows):
    results = []
    half = rows - 1
    for i in range(rows):
        spaces = " " * (half - i)
        left_nums = [str(j + 1) for j in range(i + 1)]
        right_nums = [str(j + 1) for j in range(i - 1, -1, -1)]
        left_str = " ".join(left_nums)
        right_str = " ".join(right_nums)
        line = spaces + left_str + (" " + right_str if i > 0 else "")
        results.append(line)
    return "\n".join(results)

if __name__ == '__main__':
    print(generate_symmetric_pyramid(8))