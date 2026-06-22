def hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ["*"]
    return [
        '*' * size if row == 0 or row == size - 1 else
        '*' + ' ' * (size - 2) + '*'
        for row in range(size)
    ]

if __name__ == '__main__':
    result = hollow_square(5)
    print(result)