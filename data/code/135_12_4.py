class LogicChecker:
    def are_equivalent(self, expr1, expr2):
        if expr1 == expr2:
            return True
        return not (expr1 ^ expr2)
if __name__ == '__main__':
    checker = LogicChecker()
    e1 = True
    e2 = True
    print(f"Are {e1} and {e2} equivalent? {checker.are_equivalent(e1, e2)}")
    e3 = True
    e4 = False
    print(f"Are {e3} and {e4} equivalent? {checker.are_equivalent(e3, e4)}")
    e5 = True
    e6 = False
    print(f"Are {e5} and {e6} equivalent? {checker.are_equivalent(e5, e6)}")
    e7 = False
    e8 = False
    print(f"Are {e7} and {e8} equivalent? {checker.are_equivalent(e7, e8)}")
    e9 = True
    e10 = True
    print(f"Are {e9} and {e10} equivalent? {checker.are_equivalent(e9, e10)}")