class VowelCounter:
    VOWEL_SET = frozenset("aeiouAEIOU")

    def __init__(self, text):
        self.text = text

    def get_vowel_count(self):
        count = 0
        for char in self.text:
            if char in self.VOWEL_SET:
                count += 1
        return count

def count_vowels(text):
    counter = VowelCounter(text)
    return counter.get_vowel_count()

if __name__ == '__main__':
    sample_text = "Python Programming is Fun!"
    total_vowels = count_vowels(sample_text)
    print(total_vowels)
    
    multi_counter = VowelCounter("Rhythm is funny.")
    print(multi_counter.get_vowel_count())
    
    empty_counter = VowelCounter("")
    print(empty_counter.get_vowel_count())