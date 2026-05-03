class ValueChecker:
    def are_different(self, val1, val2):
        return val1 != val2
if __name__ == '__main__':
    checker = ValueChecker()
    print(f"10 and 20 are different: {checker.are_different(10, 20)}")
    print(f"5 and 5 are different: {checker.are_different(5, 5)}")
    print(f"'hello' and 'world' are different: {checker.are_different('hello', 'world')}")
    print(f"True and False are different: {checker.are_different(True, False)}")