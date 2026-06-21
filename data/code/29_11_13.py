class VowelCounter:
    def __init__(self, text):
        self._text = text
        self._vowels = frozenset('aeiouAEIOU')

    def count_total(self):
        return sum(1 for char in self._text if char in self._vowels)

    def get_vowel_breakdown(self):
        breakdown = {char: 0 for char in 'aeiouAEIOU'}
        for char in self._text:
            if char in self._vowels:
                breakdown[char] += 1
        return {k: v for k, v in breakdown.items() if v > 0}

if __name__ == '__main__':
    sample_text = 'Python is an amazing programming language!'
    counter = VowelCounter(sample_text)
    total_vowels = counter.count_total()
    vowel_details = counter.get_vowel_breakdown()
    print(total_vowels)
    print(vowel_details)