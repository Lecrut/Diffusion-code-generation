def build_number_pyramid(height):
    rows = []
    max_width = height * 2 - 1
    for i in range(1, height + 1):
        nums = [str(j) for j in range(1, i + 1)]
        line = " ".join(nums)
        padding = (max_width - len(line)) // 2
        rows.append(" " * padding + line)
    return "\n".join(rows)

if __name__ == '__main__':
    print(build_number_pyramid(7))