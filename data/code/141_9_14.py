class Logic:
    TRUE = True
    FALSE = False

    def __init__(self, value):
        self.value = value

    @staticmethod
    def and_(value1, value2):
        return Logic(value1 and value2)

    @staticmethod
    def or_(value1, value2):
        return Logic(value1 or value2)

    @staticmethod
    def not_(value):
        return Logic(not value)
if __name__ == '__main__':
    a = Logic(True)
    b = Logic(False)
    c = Logic(Logic.TRUE)
    print(Logic.and_(a.value, b.value).value)
    print(Logic.or_(b.value, c.value).value)
    print(Logic.not_(b.value).value)