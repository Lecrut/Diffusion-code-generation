class SignAnalyzer:
    POSITIVE = "positive"
    NEGATIVE = "negative"
    ZERO = "zero"

    @staticmethod
    def _get_sign(value):
        if value > 0:
            return 1
        if value < 0:
            return -1
        return 0

    @staticmethod
    def analyze(number):
        sign_map = {
            1: SignAnalyzer.POSITIVE,
            -1: SignAnalyzer.NEGATIVE,
            0: SignAnalyzer.ZERO,
        }
        return sign_map[SignAnalyzer._get_sign(number)]

if __name__ == '__main__':
    print(SignAnalyzer.analyze(100))
    print(SignAnalyzer.analyze(-42))
    print(SignAnalyzer.analyze(0))