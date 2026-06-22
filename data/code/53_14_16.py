def reverse_number_triangle(n: int) -> str:
    return "\n".join(
        "".join(str(j + 1) for j in range(i + 1))
        for i in range(n, 0, -1)
    )

if __name__ == '__main__':
    print(reverse_number_triangle(5))