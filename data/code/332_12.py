class StringAnalyzer:
    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    sample_string = "Hello World"
    analyzer = StringAnalyzer()
    vowel_count = analyzer.count_vowels(sample_string)
    print(vowel_count)