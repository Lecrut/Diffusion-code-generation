class EqualityVerifier:
    @staticmethod
    def verify_value_equality(a, b):
        return a == b

if __name__ == '__main__':
    print(EqualityVerifier.verify_value_equality(5, 5))
    print(EqualityVerifier.verify_value_equality(5, '5'))
    print(EqualityVerifier.verify_value_equality([1, 2], [1, 2]))
    print(EqualityVerifier.verify_value_equality([1, 2], [2, 1]))