def create_repeating_pattern(word, count):
    return (word + ' ') * count

if __name__ == '__main__':
    word = 'hello'
    count = 10
    result = create_repeating_pattern(word, count)
    print(result.strip())