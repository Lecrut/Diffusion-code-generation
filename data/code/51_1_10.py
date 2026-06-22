def build_symmetric_row(number):
    sequence = list(range(1, number + 1))
    reversed_sequence = list(range(number - 1, 0, -1))
    combined = sequence + reversed_sequence
    return " ".join(str(n) for n in combined)

def generate_pyramid(levels):
    if levels < 1:
        return []
    result = []
    for i in range(1, levels + 1):
        row_content = build_symmetric_row(i)
        padding = " " * (levels - i)
        result.append(padding + row_content)
    return result

if __name__ == '__main__':
    sample_levels = 4
    output_lines = generate_pyramid(sample_levels)
    for line in output_lines:
        print(line)