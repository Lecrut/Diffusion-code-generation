class CriteriaChecker:
    MAX_VALUE = 100

    @staticmethod
    def is_positive(num):
        return num > 0

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def check_conditions(a, b, c):
        return (CriteriaChecker.is_positive(a) and 
                CriteriaChecker.is_even(b) and 
                CriteriaChecker.is_positive(c) and 
                a < CriteriaChecker.MAX_VALUE and 
                c < CriteriaChecker.MAX_VALUE)

if __name__ == '__main__':
    print(CriteriaChecker.check_conditions(5, 4, 7))