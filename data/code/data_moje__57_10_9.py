def get_fibonacci_terms(count=10):
    if count <= 0:
        return
    yield 0
    if count < 2:
        return
    yield 1
    prev, curr = 0, 1
    for _ in range(2, count):
        prev, curr = curr, prev + curr
        yield curr

if __name__ == '__main__':
    terms = list(get_fibonacci_terms(10))
    print(terms)