class SubstringSearcher:
    @staticmethod
    def contains_substring(strings, substring):
        return any(substring in string for string in strings)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    search_term = "py"
    print(f"Strings: {sample_strings}, Substring: '{search_term}'")
    print(f"Contains substring: {SubstringSearcher.contains_substring(sample_strings, search_term)}")