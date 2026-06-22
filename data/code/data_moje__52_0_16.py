def generate_diamond(n: int) -> str:
    half_diamond = []
    for i in range(n):
        spaces = " " * (n - 1 - i)
        stars = "*" * (2 * i + 1)
        half_diamond.append(f"{spaces}{stars}")
    full_diamond = half_diamond + half_diamond[-2::-1]
    return "\n".join(full_diamond)

if __name__ == '__main__':
    size = 5
    result = generate_diamond(size)
    print(result)