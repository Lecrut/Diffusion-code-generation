def repeating_pattern():
    pattern = 'ABC'
    for char in pattern:
        yield char

if __name__ == '__main__':
    generator = repeating_pattern()
    result = ''.join(next(generator) for _ in range(30))
    print(result)