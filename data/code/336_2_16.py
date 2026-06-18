class StringAnalyzer:
    def check_for_duplicates(self, text):
        seen = set()
        for char in text:
            if char in seen:
                return True
            seen.add(char)
        return False
if __name__ == '__main__':
    analyzer = StringAnalyzer()
    tests = [
        ("hello", "True"),                              
        ("abcdef", "False"),                
        ("aabbccdd", "True"),                 
        ("", "False"),                                       
        ("aa", "True")                                       
    ]
    for text, expected_str in tests:
        result = analyzer.check_for_duplicates(text)
        print(f"Text '{text}': Expected {expected_str}, Got {'True' if result else 'False'}")