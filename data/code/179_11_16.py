class StringReverser:
    REVERSED_WORDS_KEY = "reversed_words"
    
    @staticmethod
    def reverse_string(s):
        words = s.split()
        words.reverse()
        return " ".join(words)
    
    @classmethod
    def get_sample_results(cls):
        test_strings = [
            ("hello world this is a test", "test a is this world hello"),
            ("optimization is key", "key is optimization"),
            ("  leading and trailing spaces   ", "spaces trailing and leading")
        ]
        
        results = {}
        for original, expected in test_strings:
            result = cls.reverse_string(original)
            assert result == expected, f"Expected '{expected}', but got '{result}'"
            results[cls.REVERSED_WORDS_KEY] = result
        
        return results

if __name__ == '__main__':
    sample_results = StringReverser.get_sample_results()
    print(f"Original: 'hello world this is a test'")
    print(f"Reversed: '{sample_results[StringReverser.REVERSED_WORDS_KEY]}'")