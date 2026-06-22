def generate_hollow_square(n, char='#'):
    if n <= 0:
        return ""
    if n == 1:
        return char
    top_bottom = char * n
    middle = char + " " * (n - 2) + char
    rows = [top_bottom]
    for _ in range(n - 2):
        rows.append(middle)
    rows.append(top_bottom)
    return "\n".join(rows)

if __name__ == "__main__":
    sample_n = 7
    sample_char = '*'
    result = generate_hollow_square(sample_n, sample_char)
    print(result)
    default_result = generate_hollow_square(5)
    print(default_result)