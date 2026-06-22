def build_number_pyramid(height):
    lines = []
    for i in range(1, height + 1):
        num_str = str(i)
        repeat_count = 2 * i - 1
        content = f"{num_str}" * repeat_count
        padding = " " * (height - i)
        line = f"{padding}{content}{padding}"
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = build_number_pyramid(7)
    print(result)