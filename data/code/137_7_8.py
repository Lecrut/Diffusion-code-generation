class ScoreEvaluator:
    PASS_THRESHOLD = 60

    @staticmethod
    def check_status(score):
        return 'Pass' if score >= ScoreEvaluator.PASS_THRESHOLD else 'Fail'

if __name__ == '__main__':
    print(ScoreEvaluator.check_status(55))
    print(ScoreEvaluator.check_status(70))