class DuplicateChecker:
    @staticmethod
    def has_duplicates(lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            seen.add(item)
        return False

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    print(f"List {sample_list} has duplicates: {DuplicateChecker.has_duplicates(sample_list)}")