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
    test_string1 = "Hello World"
    test_string2 = "Programming is Fun"
    test_string3 = "Rhythm"
    print(f"'{test_string1}': {VowelCounter.count_vowels(test_string1)}")
    print(f"'{test_string2}': {VowelCounter.count_vowels(test_string2)}")
    print(f"'{test_string3}': {VowelCounter.count_vowels(test_string3)}")