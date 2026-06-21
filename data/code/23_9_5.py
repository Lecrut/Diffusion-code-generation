class GradeCalculator:
    BOUNDARIES = (90, 80, 70, 60, 0)
    GRADES = 'ABDCF'

    @staticmethod
    def calculate(score: int) -> str:
        if score < 0 or score > 100:
            return 'F'
        for threshold in GradeCalculator.BOUNDARIES:
            if score >= threshold:
                index = GradeCalculator.BOUNDARIES.index(threshold)
                return GradeCalculator.GRADES[index]
        return 'F'

if __name__ == '__main__':
    calc = GradeCalculator()
    print(calc.calculate(92))
    print(calc.calculate(88))
    print(calc.calculate(74))
    print(calc.calculate(61))
    print(calc.calculate(45))
    print(calc.calculate(0))