class VowelCounter:
    VOWELS = "aeiouAEIOU"

    @staticmethod
    def count_vowels(s):
        count = 0
        for char in s:
            if char in VowelCounter.VOWELS:
                count += 1
        return count

if __name__ == '__main__':
    sample_string = "Hello, World!"
    print(VowelCounter.count_vowels(sample_string))