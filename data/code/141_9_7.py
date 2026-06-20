class Logic:
    def __init__(self, value):
        self.value = value

    def and_(self, other):
        return Logic(self.value and other.value)

    def or_(self, other):
        return Logic(self.value or other.value)

    def not_(self):
        return Logic(not self.value)

if __name__ == '__main__':
    logic1 = Logic(True)
    logic2 = Logic(False)
    result_and = logic1.and_(logic2).value
    result_or = logic1.or_(logic2).value
    result_not = logic1.not_().value
    print(result_and, result_or, result_not)