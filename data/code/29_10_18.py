VOWELS_LOWER = frozenset('aeiou')
VOWELS_UPPER = frozenset('AEIOU')

def _validate_input(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

def count_vowels(text):
    _validate_input(text)
    count = 0
    for char in text:
        if char in VOWELS_LOWER or char in VOWELS_UPPER:
            count += 1
    return count

class VowelCounter:
    def __init__(self, text):
        self.text = text
    
    def get_count(self):
        return count_vowels(self.text)

if __name__ == '__main__':
    print(count_vowels("Programming"))
    print(count_vowels("123456"))
    print(count_vowels("Quick Fox"))
    print(count_vowels("aeiou"))
    counter_instance = VowelCounter("Rhythm")
    print(counter_instance.get_count())
    try:
        count_vowels(123)
    except TypeError as e:
        print(e)