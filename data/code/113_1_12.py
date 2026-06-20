class Subtractor:
    FIXED_VALUE_1 = 100
    FIXED_VALUE_2 = 50

    @staticmethod
    def subtract():
        return Subtractor.FIXED_VALUE_1 - Subtractor.FIXED_VALUE_2

if __name__ == '__main__':
    result = Subtractor.subtract()
    print(result)