def generate_star_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        pattern.append("*" * i)
    return "\n".join(pattern)
if __name__ == '__main__':
    sample_number = 5
    result = generate_star_pattern(sample_number)
    print(result)