class ValueChecker:
    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"Are 10 and 20 different? {checker.are_different(10, 20)}")
    print(f"Are 5 and 5 different? {checker.are_different(5, 5)}")
    print(f"Are 'a' and 'b' different? {checker.are_different('a', 'b')}")
    print(f"Are 3.14 and 3.1400000000000001 different? {checker.are_different(3.14, 3.1400000000000001)}")