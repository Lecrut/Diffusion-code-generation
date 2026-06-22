def generate_hollow_square(size):
    if size <= 0:
        return []
    if size == 1:
        return ['#']
    return [''.join(['#' if r == 0 or r == size - 1 or c == 0 or c == size - 1 else ' ' for c in range(size)]) for r in range(size)]

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)