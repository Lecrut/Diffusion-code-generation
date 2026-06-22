def filter_and_reverse(phrase):
    vowels = 'aeiouAEIOU'
    filtered_chars = [char for char in phrase if char not in vowels]
    reversed_chars = ''.join(filtered_chars[::-1])
    return reversed_chars

if __name__ == '__main__':
    sample_phrase = 'Python Programming!'
    result = filter_and_reverse(sample_phrase)
    print(result)