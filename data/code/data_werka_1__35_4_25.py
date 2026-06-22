def count_vowels(strings):
    vowels = set('aeiouAEIOU')
    result = {}
    for string in strings:
        count = sum(1 for char in string if char in vowels)
        result[string] = count
    return result

if __name__ == '__main__':
    sample_strings = ['hello', 'world', 'python', 'programming']
    print(count_vowels(sample_strings))