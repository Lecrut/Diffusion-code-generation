class OddDetector:
    def is_odd(self, n):
        return n & 1 == 1

if __name__ == '__main__':
    detector = OddDetector()
    print(detector.is_odd(3))
    print(detector.is_odd(4))