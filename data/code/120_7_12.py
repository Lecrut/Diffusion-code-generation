class EqualityChecker:
    @staticmethod
    def are_identical(obj1, obj2):
        return obj1 == obj2

if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 4]
    
    checker = EqualityChecker()
    result1 = checker.are_identical(list1, list2)
    print(f"list1 is identical to list2: {result1}")
    
    result2 = checker.are_identical(list1, list3)
    print(f"list1 is identical to list3: {result2}")