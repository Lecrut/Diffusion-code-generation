def build_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    full_row = "*" * size
    empty_row = "*" + " " * (size - 2) + "*"
    result = [full_row]
    for _ in range(size - 2):
        result.append(empty_row)
    result.append(full_row)
    return "\n".join(result)

if __name__ == "__main__":
    sample_size = 10
    print(build_hollow_square(sample_size))