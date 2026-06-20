class TripleChecker:
    def validate(self, x, y, z):
        if x > 0 and y > 0 and z > 0:
            if x % 2 == 0 and y % 2 == 0:
                if (x + y) % z == 0:
                    return True
        return False

if __name__ == '__main__':
    checker = TripleChecker()
    print(checker.validate(4, 8, 12))
    print(checker.validate(5, 7, 3))
    print(checker.validate(6, 10, 15))
    print(checker.validate(12, 16, 20))