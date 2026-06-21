class SetComparator:
    def __init__(self, set1, set2):
        self.set1 = set1
        self.set2 = set2

    def get_unique_to_set1(self):
        return self.set1 - self.set2

    def get_unique_to_set2(self):
        return self.set2 - self.set1

    def get_common_elements(self):
        return self.set1 & self.set2

if __name__ == '__main__':
    sample_set1 = {1, 2, 3, 4}
    sample_set2 = {3, 4, 5, 6}
    
    comparator = SetComparator(sample_set1, sample_set2)
    
    unique_to_set1 = comparator.get_unique_to_set1()
    unique_to_set2 = comparator.get_unique_to_set2()
    common_elements = comparator.get_common_elements()
    
    print(f"Unique to set 1: {unique_to_set1}")
    print(f"Unique to set 2: {unique_to_set2}")
    print(f"Common elements: {common_elements}")