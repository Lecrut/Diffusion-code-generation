class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        char_count = {}
        duplicates = []
        
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
                if char_count[char] == 2:
                    duplicates.append(char)
            else:
                char_count[char] = 1
        
        return duplicates

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string = "programming"
    print(analyzer.check_for_duplicates(sample_string))