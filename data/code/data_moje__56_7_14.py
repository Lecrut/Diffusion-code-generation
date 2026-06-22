def format_multiplication_table(base, count=10, field_width=4):
    results = []
    for i in range(1, count + 1):
        product = base * i
        line = f"{base} x {i} = {product:>{field_width}}"
        results.append(line)
    return "\n".join(results)

if __name__ == '__main__':
    sample_base = 7
    sample_count = 12
    sample_width = 5
    output = format_multiplication_table(sample_base, sample_count, sample_width)
    print(output)