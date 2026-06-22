def generate_star_pattern(size=12):
    if size <= 0:
        return []
    row = ["*"] * size
    return ["".join(row) for _ in range(size)]

if __name__ == '__main__':
    result = generate_star_pattern(12)
    print("\n".join(result))