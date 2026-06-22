def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['*']
    return [('*' if j == 0 or j == size - 1 or i == 0 or i == size - 1 else ' ') for i in range(size)]

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)