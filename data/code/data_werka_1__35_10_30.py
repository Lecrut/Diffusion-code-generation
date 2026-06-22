class VowelCounter:
    def __init__(self):
        self.vowels = "aeiou"

    def count(self, text):
        return sum(1 for char in text if char.lower() in self.vowels)

if __name__ == '__main__':
    counter = VowelCounter()
    test_string_1 = "Hello World"
    result_1 = counter.count(test_string_1)
    print(result_1)
    
    test_string_2 = "Programming is Fun"
    result_2 = counter.count(test_string_2)
    print(result_2)
    
    test_string_3 = "AEIOUaeiou"
    result_3 = counter.count(test_string_3)
    print(result_3)
    
    test_string_4 = "Alibaba Cloud"
    result_4 = counter.count(test_string_4)
    print(result_4)
    
    test_string_5 = "Object-Oriented Programming"
    result_5 = counter.count(test_string_5)
    print(result_5)