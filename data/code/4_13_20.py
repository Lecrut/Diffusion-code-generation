class ConsonantCounter:
    CONSONANTS = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    @staticmethod
    def count(text):
        return sum(1 for char in text if char in ConsonantCounter.CONSONANTS)

if __name__ == '__main__':
    sample = "Programming is fun!"
    print(ConsonantCounter.count(sample))