def hollow_square(size: int) -> list[str]:
    if size <= 0:
        return []
    return ['*' * size if i == 0 or i == size - 1 else '*' + ' ' * (size - 2) + '*' for i in range(size)]

if __name__ == '__main__':
    print(hollow_square(5))