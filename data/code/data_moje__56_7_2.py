def format_multiplication_table(base, max_multiplier=12):
    width = len(str(base * max_multiplier)) + 1
    lines = []
    for multiplier in range(1, max_multiplier + 1):
        product = base * multiplier
        line = "{} x {} = {:>{}}".format(base, multiplier, product, width)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    base = 7
    result = format_multiplication_table(base)
    print(result)