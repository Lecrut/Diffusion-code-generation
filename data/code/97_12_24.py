def compute_xor_table():
    inputs = [0, 1]
    table = []
    for a in inputs:
        for b in inputs:
            result = a ^ b
            table.append((a, b, result))
    return table

def format_table(rows):
    header = "A | B | XOR"
    separator = "---+---+---"
    lines = [header, separator]
    for a, b, res in rows:
        lines.append(f"{a} | {b} | {res}")
    return "\n".join(lines)

if __name__ == '__main__':
    rows = compute_xor_table()
    output = format_table(rows)
    print(output)