def build_reverse_triangle(n):
    return "\n".join([("  " * i) + "* " * (n - i) for i in range(n)])

if __name__ == "__main__":
    sample_size = 5
    result = build_reverse_triangle(sample_size)
    print(result)