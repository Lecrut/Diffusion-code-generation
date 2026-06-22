class UniqueSubstringsFinder:
    MIN_LENGTH = 3

    @staticmethod
    def find_unique_substrings(input_string):
        substrings_set = set()
        length = len(input_string)
        
        for start in range(length):
            for end in range(start + self.MIN_LENGTH, length + 1):
                substring = input_string[start:end]
                substrings_set.add(substring)
                
        return substrings_set

if __name__ == '__main__':
    sample_string = "abcde"
    finder = UniqueSubstringsFinder()
    unique_substrings = finder.find_unique_substrings(sample_string)
    print(unique_substrings)