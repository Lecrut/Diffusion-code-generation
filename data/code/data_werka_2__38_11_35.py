class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        char_count = {}
        duplicates = set()
        
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
                duplicates.add(char)
            else:
                char_count[char] = 1
        
        return list(duplicates)

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string = "programming"
    result = analyzer.check_for_duplicates(sample_string)
    print(result)