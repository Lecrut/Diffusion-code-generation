import collections
def vowel_frequency_map(text):
    frequency = collections.defaultdict(int)
    text = text.lower()
    vowels = "aeiou"
    for char in text:
        if char in vowels and 'a' <= char <= 'z':
            frequency[char] += 1
    return dict(frequency)
if __name__ == '__main__':
    sample_string = "Programming is Awesome"
    result = vowel_frequency_map(sample_string)
    print(result)