def hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    return [
        '*' * size if i == 0 or i == size - 1 else '*' + ' ' * (size - 2) + '*'
        for i in range(size)
    ]

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(3))
    print(hollow_square(0))