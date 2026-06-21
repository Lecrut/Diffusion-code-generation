def count_vowels(text):
    vowels = set('aeiouAEIOU')
    unique_chars = set(text)
    intersection = unique_chars.intersection(vowels)
    return sum(text.count(v) for v in intersection)

if __name__ == '__main__':
    sample_text = "Hello World"
    result = count_vowels(sample_text)
    print(result)