class StringProcessor:
    def remove_all_whitespace(self, input_string: str) -> str:
        return input_string.translate(str.maketrans('', '', ' \t\n\r\f\v'))

if __name__ == '__main__':
    processor = StringProcessor()
    sample1 = "Hello World\nThis has\tmixed spaces."
    sample2 = "Unicode: \u20AC and some spaces\tand newlines\n\r"
    sample3 = "NoWhitespaceHere"
    sample4 = "\t\n  Multiple\tspaces\r\n"
    sample5 = "   \t\n"
    
    print(f"Original 1: '{sample1}'")
    result1 = processor.remove_all_whitespace(sample1)
    print(f"Result 1:   '{result1}'\n")
    
    print(f"Original 2: '{sample2}'")
    result2 = processor.remove_all_whitespace(sample2)
    print(f"Result 2:   '{result2}'\n")
    
    print(f"Original 3: '{sample3}'")
    result3 = processor.remove_all_whitespace(sample3)
    print(f"Result 3:   '{result3}'\n")
    
    print(f"Original 4: '{sample4}'")
    result4 = processor.remove_all_whitespace(sample4)
    print(f"Result 4:   '{result4}'\n")
    
    print(f"Original 5: '{sample5}'")
    result5 = processor.remove_all_whitespace(sample5)
    print(f"Result 5:   '{result5}'\n")