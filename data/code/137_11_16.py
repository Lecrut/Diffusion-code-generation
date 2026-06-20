class DuplicateChecker:

    def has_duplicates(self, lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            seen.add(item)
        return False
if __name__ == '__main__':
    checker = DuplicateChecker()
    print(checker.has_duplicates([1, 2, 3, 4]))
    print(checker.has_duplicates([1, 2, 3, 2]))