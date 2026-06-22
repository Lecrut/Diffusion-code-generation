def format_multiplication_table(base, multiplier_range):
    max_value = max(base * m for m in multiplier_range)
    width = len(str(max_value))
    lines = []
    for multiplier in multiplier_range:
        result = base * multiplier
        line = "{} x {:>{width}} = {:>{width}}".format(
            base, multiplier, result, width=width
        )
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    base_number = 7
    multipliers = range(1, 11)
    result = format_multiplication_table(base_number, multipliers)
    print(result)