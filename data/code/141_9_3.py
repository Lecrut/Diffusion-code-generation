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
    print(a.and_(b).value)
    print(a.or_(b).value)
    print(a.not_().value)