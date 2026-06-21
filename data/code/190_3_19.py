class MembershipChecker:
    @staticmethod
    def check(iterable, value):
        return value in iterable

if __name__ == '__main__':
    checker = MembershipChecker()
    list1 = [1.1, 2.2, 3.3, 4.4, 5.5]
    value1 = 3.3
    result1 = checker.check(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")
    
    list2 = [6.6, 7.7, 8.8]
    value2 = 9.9
    result2 = checker.check(list2, value2)
    print(f"Is {value2} in {list2}? {result2}")