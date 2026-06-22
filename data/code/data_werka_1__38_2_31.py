class StringAnalyzer:
    def __init__(self):
        self.seen = set()
        self.duplicates = set()

    def check_for_duplicates(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        
        self.seen.clear()
        self.duplicates.clear()
        
        for char in input_string:
            if char in self.seen:
                self.duplicates.add(char)
            else:
                self.seen.add(char)
        
        return sorted(list(self.duplicates))

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string_1 = "hello world"
    sample_string_2 = "programming"
    sample_string_3 = "abcdefg"
    sample_string_4 = "aabbccddeeff"
    
    try:
        result_1 = analyzer.check_for_duplicates(sample_string_1)
        print(f"Input: '{sample_string_1}', Duplicates: {result_1}")
        
        result_2 = analyzer.check_for_duplicates(sample_string_2)
        print(f"Input: '{sample_string_2}', Duplicates: {result_2}")
        
        result_3 = analyzer.check_for_duplicates(sample_string_3)
        print(f"Input: '{sample_string_3}', Duplicates: {result_3}")
        
        result_4 = analyzer.check_for_duplicates(sample_string_4)
        print(f"Input: '{sample_string_4}', Duplicates: {result_4}")
    except ValueError as e:
        print(e)