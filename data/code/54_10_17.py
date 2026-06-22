def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    row_full = "*" * size
    row_hollow = "*" + " " * (size - 2) + "*"
    return [row_full if i == 0 or i == size - 1 else row_hollow for i in range(size)]

if __name__ == '__main__':
    print(generate_hollow_square(5))