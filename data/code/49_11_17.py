def generate_asterisk_square(size: int) -> str:
    return "\n".join(["*" * size for _ in range(size)])

if __name__ == "__main__":
    print(generate_asterisk_square(10))