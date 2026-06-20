class ScoreChecker:
    PASS_THRESHOLD = 60

    @staticmethod
    def check_status(score):
        return 'Pass' if score >= ScoreChecker.PASS_THRESHOLD else 'Fail'

if __name__ == '__main__':
    print(ScoreChecker.check_status(55))
    print(ScoreChecker.check_status(70))