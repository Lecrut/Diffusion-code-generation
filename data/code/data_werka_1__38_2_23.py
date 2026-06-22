class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        
        seen = {}
        duplicates = set()
        
        for char in input_string:
            if char in seen:
                seen[char] += 1
                duplicates.add(char)
            else:
                seen[char] = 1
        
        return sorted(list(duplicates))

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    
    sample_strings = [
        "hello world",
        "programming",
        "abcdefg",
        "aabbccddeeff",
        "mississippi"
    ]
    
    for sample in sample_strings:
        print(f"Input: '{sample}', Duplicates: {analyzer.check_for_duplicates(sample)}")