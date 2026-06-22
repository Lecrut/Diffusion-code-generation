def repeat_pattern():
    pattern = 'ABC'
    while True:
        for char in pattern:
            yield char

if __name__ == '__main__':
    gen = repeat_pattern()
    result = ''.join(next(gen) for _ in range(30))
    print(result)