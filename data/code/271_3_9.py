class SubstringFinder:
    MIN_LENGTH = 3

    @staticmethod
    def find_unique_substrings(input_string):
        substrings = set()
        length = len(input_string)
        for i in range(length):
            for j in range(i + SubstringFinder.MIN_LENGTH, length + 1):
                substring = input_string[i:j]
                if len(substring) >= SubstringFinder.MIN_LENGTH:
                    substrings.add(substring)
        return substrings

if __name__ == '__main__':
    sample_string = "abcde"
    finder = SubstringFinder()
    unique_substrings = finder.find_unique_substrings(sample_string)
    print(unique_substrings)