class StringDoubler:
    @staticmethod
    def double_characters(input_string):
        return ''.join(char * 2 for char in input_string)

if __name__ == '__main__':
    doubler = StringDoubler()
    sample1 = "abc"
    result1 = doubler.double_characters(sample1)
    print(f"Input: {sample1}, Result: {result1}")
    
    sample2 = "hello"
    result2 = doubler.double_characters(sample2)
    print(f"Input: {sample2}, Result: {result2}")