CHARSET_MAP = {
    "star": "*",
    "dot": ".",
    "hash": "#"
}

def generate_left_aligned_triangle(rows, symbol_key="star"):
    symbol = CHARSET_MAP[symbol_key]
    lines = []
    for i in range(1, rows + 1):
        lines.append(symbol * i)
    return "\n".join(lines)

if __name__ == '__main__':
    result = generate_left_aligned_triangle(15, "star")
    print(result)