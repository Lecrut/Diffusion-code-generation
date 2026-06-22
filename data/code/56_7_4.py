def format_multiplication_table(base, limit=10, field_width=4):
    result = []
    for i in range(1, limit + 1):
        product = base * i
        result.append(f"{base} x {i} = {product:>{field_width}}")
    return "\n".join(result)

if __name__ == '__main__':
    sample_base = 7
    sample_limit = 12
    print(format_multiplication_table(sample_base, sample_limit, 5))