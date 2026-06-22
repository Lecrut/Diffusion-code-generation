def generate_number_pyramid(size: int) -> list[str]:
    return [
        " " * (size - row) + " ".join(str(num) for num in range(1, row + 1))
        for row in range(1, size + 1)
    ]

if __name__ == "__main__":
    fixed_size = 6
    result = generate_number_pyramid(fixed_size)
    print(result)