class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        seen_characters = {}
        duplicates = set()
        
        for char in input_string:
            if char in seen_characters:
                seen_characters[char] += 1
                if seen_characters[char] == 2:
                    duplicates.add(char)
            else:
                seen_characters[char] = 1
        
        return sorted(list(duplicates))

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    sample_string_1 = "hello world"
    sample_string_2 = "programming"
    sample_string_3 = "abcdefg"
    sample_string_4 = "aabbccddeeff"
    
    result_1 = analyzer.check_for_duplicates(sample_string_1)
    print(f"Input: '{sample_string_1}', Duplicates: {result_1}")
    
    result_2 = analyzer.check_for_duplicates(sample_string_2)
    print(f"Input: '{sample_string_2}', Duplicates: {result_2}")
    
    result_3 = analyzer.check_for_duplicates(sample_string_3)
    print(f"Input: '{sample_string_3}', Duplicates: {result_3}")
    
    result_4 = analyzer.check_for_duplicates(sample_string_4)
    print(f"Input: '{sample_string_4}', Duplicates: {result_4}")