class StringAnalyzer:
    def has_repeated_letters(self, text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        seen = set()
        for char in text:
            if char in seen:
                return True
            seen.add(char)
        return False

if __name__ == '__main__':
    analyzer = StringAnalyzer()
    sample_string1 = "hello world"
    sample_string2 = "programming"
    sample_string3 = "abcdefg"
    sample_string4 = "aabbccddeeff"
    
    print(f"'{sample_string1}' has repeated letters: {analyzer.has_repeated_letters(sample_string1)}")
    print(f"'{sample_string2}' has repeated letters: {analyzer.has_repeated_letters(sample_string2)}")
    print(f"'{sample_string3}' has repeated letters: {analyzer.has_repeated_letters(sample_string3)}")
    print(f"'{sample_string4}' has repeated letters: {analyzer.has_repeated_letters(sample_string4)}")