class StringSplitter:
    def split_characters(self, input_string):
        return list(input_string)

if __name__ == '__main__':
    splitter = StringSplitter()
    sample1 = "hello"
    result1 = splitter.split_characters(sample1)
    print(f"Input: {sample1}, Output: {result1}")
    
    sample2 = "world"
    result2 = splitter.split_characters(sample2)
    print(f"Input: {sample2}, Output: {result2}")
    
    sample3 = ""
    result3 = splitter.split_characters(sample3)
    print(f"Input: {sample3}, Output: {result3}")
    
    sample4 = "Python"
    result4 = splitter.split_characters(sample4)
    print(f"Input: {sample4}, Output: {result4}")