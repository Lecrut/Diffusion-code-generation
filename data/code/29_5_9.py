import re

def vowel_count_generator(sentences):
    vowels = set('aeiouAEIOU')
    for sentence in sentences:
        words = re.findall(r"\b\w+\b", sentence)
        for word in words:
            count = sum(1 for char in word if char in vowels)
            yield count

if __name__ == '__main__':
    sentences = [
        "Hello World",
        "Python is awesome",
        "Count the vowels"
    ]
    results = list(vowel_count_generator(sentences))
    print(results)