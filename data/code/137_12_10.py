class MaxFinder:

    @staticmethod
    def max_of_three(a, b, c):
        return a if a >= b and a >= c else b if b >= a and b >= c else c
if __name__ == '__main__':
    print(MaxFinder.max_of_three(10, 20, 30))
    print(MaxFinder.max_of_three(5, 15, 10))
    print(MaxFinder.max_of_three(-5, -10, -3))