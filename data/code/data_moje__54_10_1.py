def hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    return ["*" * i + "*" + " " * (size - 2) + "*" + "*" * (size - 1 - i) if i == 0 or i == size - 1 else "*" * i + "*" + " " * (size - 2) + "*" + "*" * (size - 1 - i) for i in range(size)]

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(3))