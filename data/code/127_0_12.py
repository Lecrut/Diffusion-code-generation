class OddDetector:
    @staticmethod
    def is_odd(n):
        return n & 1

if __name__ == '__main__':
    num = 25
    result = OddDetector.is_odd(num)
    print(result)