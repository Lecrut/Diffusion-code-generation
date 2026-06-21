class StringSplitter:
    DELIMITER = ''
    
    @staticmethod
    def split_string(input_string):
        return list(input_string)

if __name__ == '__main__':
    splitter = StringSplitter()
    sample_string_1 = "hello"
    result_1 = splitter.split_string(sample_string_1)
    print(f"Input: {sample_string_1}, Output: {result_1}")
    
    sample_string_2 = "world"
    result_2 = splitter.split_string(sample_string_2)
    print(f"Input: {sample_string_2}, Output: {result_2}")
    
    sample_string_3 = "Python"
    result_3 = splitter.split_string(sample_string_3)
    print(f"Input: {sample_string_3}, Output: {result_3}")