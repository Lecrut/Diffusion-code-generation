def generate_hollow_square(size):
    if size <= 0:
        return ""
    if size == 1:
        return "*"
    first_row = "*" * size
    middle_row = "*" + " " * (size - 2) + "*"
    result = [first_row]
    for _ in range(size - 2):
        result.append(middle_row)
    result.append(first_row)
    return "\n".join(result)

if __name__ == '__main__':
    print(generate_hollow_square(5))