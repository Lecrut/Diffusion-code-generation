def has_valid_prefix(strings):
    prefix_map = {'A': True, 'B': True}
    for text in strings:
        if text and text[0] in prefix_map:
            return True
    return False

if __name__ == '__main__':
    words = ['Apple', 'Banana', 'Cherry']
    print(has_valid_prefix(words))