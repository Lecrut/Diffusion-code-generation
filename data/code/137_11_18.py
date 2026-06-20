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
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"List {sample_list1}: {DuplicateChecker.has_duplicates(sample_list1)}")

    sample_list2 = [1, 2, 3, 3, 4]
    print(f"List {sample_list2}: {DuplicateChecker.has_duplicates(sample_list2)}")