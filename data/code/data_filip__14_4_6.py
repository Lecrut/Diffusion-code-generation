class DuplicateChecker:
    def __init__(self, target_string):
        self.target_string = target_string

    def has_duplicates(self):
        return len(self.target_string) != len(set(self.target_string))

    def get_duplicate_count(self):
        if self.has_duplicates():
            seen = set()
            duplicates = set()
            for char in self.target_string:
                if char in seen:
                    duplicates.add(char)
                else:
                    seen.add(char)
            return len(duplicates)
        return 0

if __name__ == '__main__':
    checker1 = DuplicateChecker("banana")
    checker2 = DuplicateChecker("python")
    print(checker1.has_duplicates())
    print(checker2.get_duplicate_count())
    print(checker1.get_duplicate_count())