class ConsonantCounter:
    VOWELS = frozenset({'a', 'e', 'i', 'o', 'u'})

    @staticmethod
    def count(text):
        counter = 0
        for character in text:
            if character.isalpha() and character.lower() not in ConsonantCounter.VOWELS:
                counter += 1
        return counter

if __name__ == '__main__':
    sample = "Python is great! 42"
    result = ConsonantCounter.count(sample)
    print(result)