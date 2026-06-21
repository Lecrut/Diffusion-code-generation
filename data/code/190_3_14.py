class MembershipChecker:
    @staticmethod
    def check(iterable, value):
        return value in iterable

if __name__ == '__main__':
    checker = MembershipChecker()
    list1 = [1.1, 2.2, 3.3]
    value1 = 2.2
    result1 = checker.check(list1, value1)
    print(f"Is {value1} in {list1}? {result1}")
    
    tuple1 = (4.4, 5.5, 6.6)
    value2 = 7.7
    result2 = checker.check(tuple1, value2)
    print(f"Is {value2} in {tuple1}? {result2}")