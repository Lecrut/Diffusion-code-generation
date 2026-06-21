class Grader:
    GRADES = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]

    def get_grade(self, score):
        return next(g for t, g in self.GRADES if score >= t)

if __name__ == '__main__':
    grader = Grader()
    print(grader.get_grade(95))
    print(grader.get_grade(85))
    print(grader.get_grade(75))
    print(grader.get_grade(65))
    print(grader.get_grade(55))