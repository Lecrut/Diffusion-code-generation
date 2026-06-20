class OddChecker:
    @staticmethod
    def is_odd(number):
        return number & 1 == 1

if __name__ == '__main__':
    print("Is 4 odd?", OddChecker.is_odd(4))
    print("Is 5 odd?", OddChecker.is_odd(5))