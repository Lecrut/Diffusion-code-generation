def growing_numbers(N):
    for i in range(1, N + 1):
        yield i

if __name__ == '__main__':
    print(list(growing_numbers(5)))