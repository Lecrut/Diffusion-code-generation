class UniqueElementsChecker:
    def __init__(self, lst):
        self.lst = lst

    def are_elements_unique(self):
        seen = set()
        for item in self.lst:
            if item in seen:
                return False
            seen.add(item)
        return True

if __name__ == '__main__':
    checker1 = UniqueElementsChecker([1, 2, 3, 4, 5])
    print(checker1.are_elements_unique())
    
    checker2 = UniqueElementsChecker([1, 2, 3, 3, 5])
    print(checker2.are_elements_unique())