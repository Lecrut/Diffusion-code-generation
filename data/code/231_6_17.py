def create_repeating_pattern(word, count):
    return ' '.join([word] * count)

if __name__ == '__main__':
    word = 'hello'
    count = 10
    result = create_repeating_pattern(word, count)
    print(result)