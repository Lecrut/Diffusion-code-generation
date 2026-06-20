class Grading:
    def check_status(self, score):
        return 'Pass' if score >= 60 else 'Fail'

if __name__ == '__main__':
    grader = Grading()
    print(grader.check_status(55))
    print(grader.check_status(70))