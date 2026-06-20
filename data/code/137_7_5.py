class ScoreEvaluator:
    def check_status(self, score):
        return 'Pass' if score >= 60 else 'Fail'

if __name__ == '__main__':
    evaluator = ScoreEvaluator()
    print(evaluator.check_status(55))
    print(evaluator.check_status(70))