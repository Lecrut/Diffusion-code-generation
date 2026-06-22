class TripletValidator:
    MIN_VALUE = 0
    MAX_VALUE = 100
    REQUIRED_MODULUS = 2

    @staticmethod
    def is_valid_number(value):
        return value > TripletValidator.MIN_VALUE and value < TripletValidator.MAX_VALUE and value % TripletValidator.REQUIRED_MODULUS == 0

    @staticmethod
    def check_all(a, b, c):
        return TripletValidator.is_valid_number(a) and TripletValidator.is_valid_number(b) and TripletValidator.is_valid_number(c)

if __name__ == '__main__':
    print(TripletValidator.check_all(2, 4, 6))
    print(TripletValidator.check_all(2, 4, 102))
    print(TripletValidator.check_all(2, 3, 4))
    print(TripletValidator.check_all(-2, 4, 6))