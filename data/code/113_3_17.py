class Subtracter:
    MINUS_ONE = -1

    @staticmethod
    def subtract(a):
        return a + Subtracter.MINUS_ONE

if __name__ == '__main__':
    print(Subtracter.subtract(5))