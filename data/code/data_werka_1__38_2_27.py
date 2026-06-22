class StringAnalyzer:
    def check_for_duplicates(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        
        seen = set()
        duplicates = set()
        for char in input_string:
            if char in seen:
                duplicates.add(char)
            else:
                seen.add(char)
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
    
    for s in sample_strings:
        try:
            result = analyzer.check_for_duplicates(s)
            print(f"Input: '{s}', Duplicates: {result}")
        except ValueError as e:
            print(e)