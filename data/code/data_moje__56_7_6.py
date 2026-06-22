def format_multiplication_table(base, width=4):
    lines = []
    for multiplier in range(1, 11):
        product = base * multiplier
        line = "{:<{w}} x {:<{w}} = {:<{w}}".format(base, multiplier, product, w=width)
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    result = format_multiplication_table(7)
    print(result)