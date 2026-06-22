class LexicographicalMinFinder:
    def find_min(self, strings):
        if not all(isinstance(s, str) for s in strings):
            raise ValueError("All elements in the list must be strings")
        return min(strings)

if __name__ == '__main__':
    finder = LexicographicalMinFinder()
    sample_strings = ["apple", "banana", "cherry", "date"]
    result = finder.find_min(sample_strings)
    print(f"Minimum lexicographical string: {result}")