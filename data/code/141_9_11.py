class Logic:
    TRUE = True
    FALSE = False

    def __init__(self, value):
        self.value = value

    @staticmethod
    def and_(a, b):
        return Logic(a.value and b.value)

    @staticmethod
    def or_(a, b):
        return Logic(a.value or b.value)

    @staticmethod
    def not_(value):
        return Logic(not value.value)

if __name__ == '__main__':
    a = Logic(Logic.TRUE)
    b = Logic(Logic.FALSE)
    print(Logic.and_(a, b).value)
    print(Logic.or_(a, b).value)
    print(Logic.not_(b).value)