class NumberAnalyzer:
    VALUES = (88, 42, 93)

    @staticmethod
    def get_max():
        a, b, c = NumberAnalyzer.VALUES
        return a if a >= b and a >= c else (b if b >= c else c)

if __name__ == '__main__':
    print(NumberAnalyzer.get_max())