class StringDoubler:
    def double_characters(self, text):
        return ''.join(char * 2 for char in text)

if __name__ == '__main__':
    doubler = StringDoubler()
    text1 = 'abc'
    result1 = doubler.double_characters(text1)
    print(f"Text: {text1}, Result: {result1}")
    
    text2 = 'hello'
    result2 = doubler.double_characters(text2)
    print(f"Text: {text2}, Result: {result2}")