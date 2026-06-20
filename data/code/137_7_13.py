class ScoreChecker:
    def check_status(self, score):
        return 'Pass' if score >= 60 else 'Fail'

if __name__ == '__main__':
    checker = ScoreChecker()
    print(checker.check_status(55))
    print(checker.check_status(70))