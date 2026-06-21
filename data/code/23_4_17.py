class GradePolicy:
    def get_grade(self, score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

class StudentGrader:
    def __init__(self, policy):
        self.policy = policy

    def determine_letter_grade(self, score):
        return self.policy.get_grade(score)

if __name__ == '__main__':
    policy = GradePolicy()
    grader = StudentGrader(policy)
    print(grader.determine_letter_grade(92))
    print(grader.determine_letter_grade(85))
    print(grader.determine_letter_grade(74))
    print(grader.determine_letter_grade(65))
    print(grader.determine_letter_grade(50))