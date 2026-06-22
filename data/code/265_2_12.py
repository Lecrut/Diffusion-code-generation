def unique_chars(phrase):
    char_count = {}
    for char in phrase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return ''.join([char for char in phrase if char_count[char] == 1])

if __name__ == '__main__':
    print(unique_chars("programming"))