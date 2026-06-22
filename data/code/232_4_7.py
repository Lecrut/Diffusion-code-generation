def generate_growing_numbers(n):
    for i in range(1, n + 1):
        yield i

if __name__ == '__main__':
    print(list(generate_growing_numbers(5)))