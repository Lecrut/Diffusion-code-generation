class StringRepeater:
    def repeat_characters(self, string):
        return ''.join(char * 2 for char in string)

if __name__ == '__main__':
    repeater = StringRepeater()
    sample1 = "abc"
    result1 = repeater.repeat_characters(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    
    sample2 = "hello"
    result2 = repeater.repeat_characters(sample2)
    print(f"Input: {sample2}, Output: {result2}")