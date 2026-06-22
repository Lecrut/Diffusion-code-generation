class IntegerListHandler:
    _DATA = [7, 14, 21, 28, 35]

    @staticmethod
    def get_first():
        return IntegerListHandler._DATA[0]

if __name__ == '__main__':
    result = IntegerListHandler.get_first()
    print(result)