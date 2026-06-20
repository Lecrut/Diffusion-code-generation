import unittest

class CheckBothFalse:
    @staticmethod
    def check(a, b):
        return not a and not b
    
    @classmethod
    def test(cls):
        assert cls.check(False, False) == True
        assert cls.check(True, False) == False
        assert cls.check(False, True) == False
        assert cls.check(True, True) == False

if __name__ == '__main__':
    CheckBothFalse.test()
    print(CheckBothFalse.check(False, False))
    print(CheckBothFalse.check(True, False))
    print(CheckBothFalse.check(False, True))
    print(CheckBothFalse.check(True, True))