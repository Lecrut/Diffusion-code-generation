class Grading:
    PASS_THRESHOLD = 60
    STATUS_PASS = 'Pass'
    STATUS_FAIL = 'Fail'

    @staticmethod
    def check_status(score):
        return Grading.STATUS_PASS if score >= Grading.PASS_THRESHOLD else Grading.STATUS_FAIL

if __name__ == '__main__':
    print(Grading.check_status(55))
    print(Grading.check_status(70))