class StringProcessor:
    def reverse_word_order(self, text: str) -> str:
        words = text.split()
        words.reverse()
        return " ".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "hello world this is a test"
    result1 = processor.reverse_word_order(sample_string1)
    print(f"Original: '{sample_string1}'")
    print(f"Reversed: '{result1}'")
    sample_string2 = "  leading and trailing spaces   "
    result2 = processor.reverse_word_order(sample_string2)
    print(f"Original: '{sample_string2}'")
    print(f"Reversed: '{result2}'")
    sample_string3 = "singleword"
    result3 = processor.reverse_word_order(sample_string3)
    print(f"Original: '{sample_string3}'")
    print(f"Reversed: '{result3}'")