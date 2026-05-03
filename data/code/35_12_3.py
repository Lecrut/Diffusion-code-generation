class VowelCounter:
    def count(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count
if __name__ == '__main__':
    counter = VowelCounter()
    sample_text1 = "Hello World"
    sample_text2 = "Programming is Fun"
    sample_text3 = "AEIOUaeiou123"
    result1 = counter.count(sample_text1)
    result2 = counter.count(sample_text2)
    result3 = counter.count(sample_text3)
    print(f"'{sample_text1}' has {result1} vowels.")
    print(f"'{sample_text2}' has {result2} vowels.")
    print(f"'{sample_text3}' has {result3} vowels.")