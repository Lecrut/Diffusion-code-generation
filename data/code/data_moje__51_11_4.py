def generate_centered_number_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        num = i
        row_num_str = str(num)
        row_str = ""
        for _ in range(num):
            row_str += row_num_str
        spaces = " " * (height - i)
        lines.append(f"{spaces}{row_str}{spaces}")
    return "\n".join(lines)

if __name__ == '__main__':
    height = 7
    result = generate_centered_number_pyramid(height)
    print(result)