def print_triangle(height: int) -> None:
    for i in range(1, height + 1):
        print("*" * i)

if __name__ == "__main__":
    SAMPLE_HEIGHT = 5
    print_triangle(SAMPLE_HEIGHT)