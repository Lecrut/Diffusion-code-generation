def format_multiplication_table(base: int, start: int = 1, end: int = 10) -> str:
    if base < 0:
        base = -base
    if start < 1:
        start = 1
    if end < start:
        end = start
    field_width = max(len(str(base * end)), len(str(start)), len(str(end)), 2)
    lines = []
    for i in range(start, end + 1):
        product = base * i
        line = f"{base} x {i:>{field_width - len(str(i))}} = {product:>{field_width}}".strip()
        lines.append(line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(format_multiplication_table(base=7, start=1, end=12))