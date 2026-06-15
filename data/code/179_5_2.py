class StringProcessor:
    def reverse_word_order(self, text: str) -> str:
        words = text.split()
        words.reverse()
        return " ".join(words)
if __name__ == '__main__':
    processor = StringProcessor()
    sample_string1 = "hello world this is a test"
    sample_string2 = "  leading and trailing spaces  "
    sample_string3 = "singleword"
    sample_string4 = ""
    result1 = processor.reverse_word_order(sample_string1)
    result2 = processor.reverse_word_order(sample_string2)
    result3 = processor.reverse_word_order(sample_string3)
    result4 = processor.reverse_word_order(sample_string4)
    print(f"'{sample_string1}' -> '{result1}'")
    print(f"'{sample_string2}' -> '{result2}'")
    print(f"'{sample_string3}' -> '{result3}'")
    print(f"'{sample_string4}' -> '{result4}'")