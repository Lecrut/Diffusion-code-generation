class SignAnalyzer:
    POSITIVE = "positive"
    NEGATIVE = "negative"
    ZERO = "zero"

    @staticmethod
    def determine_sign(number):
        if number > 0:
            return SignAnalyzer.POSITIVE
        if number < 0:
            return SignAnalyzer.NEGATIVE
        return SignAnalyzer.ZERO

if __name__ == '__main__':
    analyzer = SignAnalyzer()
    print(analyzer.determine_sign(15))
    print(analyzer.determine_sign(-8))
    print(analyzer.determine_sign(0))