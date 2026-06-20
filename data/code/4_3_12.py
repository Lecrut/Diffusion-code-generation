class ConsonantCounter:
    VOWELS = set("aeiouAEIOU")

    @staticmethod
    def count(text):
        consonants = [c for c in text if c.isalpha() and c not in ConsonantCounter.VOWELS]
        return len(consonants)

if __name__ == '__main__':
    sample_text = "Python Programming 2024!"
    result = ConsonantCounter.count(sample_text)
    print(result)