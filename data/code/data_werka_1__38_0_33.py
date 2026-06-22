class RepeatedLetterFinder:
    def __init__(self, input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        self.input_string = input_string

    def find_repeated_letters(self):
        seen_letters = set()
        repeated_letters = set()
        for char in self.input_string:
            lower_char = char.lower()
            if 'a' <= lower_char <= 'z':
                if lower_char in seen_letters:
                    repeated_letters.add(lower_char)
                else:
                    seen_letters.add(lower_char)
        return sorted(list(repeated_letters))

if __name__ == '__main__':
    sample_strings = ["programming", "hello world", "123abcABC", "!@#$$%^&*()", "aabbcc"]
    for s in sample_strings:
        try:
            finder = RepeatedLetterFinder(s)
            repeated = finder.find_repeated_letters()
            print(f"Repeated letters in '{s}': {repeated}")
        except ValueError as e:
            print(e)