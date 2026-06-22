def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    return ["".join(["*" if i == 0 or i == size - 1 or j == 0 or j == size - 1 else " " for j in range(size)]) for i in range(size)]

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)