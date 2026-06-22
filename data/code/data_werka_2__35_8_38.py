class VowelCounter:
    VOWELS = 'aeiouAEIOU'

    @staticmethod
    def count_vowels(input_string):
        return sum(1 for char in input_string if char in VowelCounter.VOWELS)

if __name__ == '__main__':
    sample_input_1 = "Hello, World!"
    sample_input_2 = "Python Programming"
    sample_input_3 = "Alibaba Cloud"
    
    print(VowelCounter.count_vowels(sample_input_1))
    print(VowelCounter.count_vowels(sample_input_2))
    print(VowelCounter.count_vowels(sample_input_3))