class OddChecker:
    @staticmethod
    def is_odd(n):
        return n & 1

if __name__ == '__main__':
    result = OddChecker.is_odd(3)
    print(result)
    result = OddChecker.is_odd(4)
    print(result)