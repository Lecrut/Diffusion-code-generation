import collections

def count_vowels(text):
    vowels = frozenset('aeiouAEIOU')
    counter = collections.Counter(char for char in text if char in vowels)
    return sum(counter.values())

if __name__ == '__main__':
    sample_text = 'Programming with Python is efficient and powerful.'
    result = count_vowels(sample_text)
    print(result)