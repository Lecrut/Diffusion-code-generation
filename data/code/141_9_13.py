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
    x = Logic(True)
    y = Logic(False)
    z = Logic(True)
    print(x.and_(y).and_(z).value)
    print(x.or_(y).or_(z).value)
    print(y.not_().not_().value)