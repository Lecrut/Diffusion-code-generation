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
    a = Logic(True)
    b = Logic(False)
    c = Logic(True)
    result_and = a.and_(b).and_(c).value
    result_or = a.or_(b).or_(c).value
    result_not = b.not_().not_().value
    print(result_and)
    print(result_or)
    print(result_not)