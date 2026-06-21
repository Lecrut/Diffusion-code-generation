class MaxFinder:
    COMPARISON_TYPE = "max"

    @staticmethod
    def find_greatest(a, b, c):
        return a if a >= b and a >= c else b if b >= c else c

def greatest_of_three(a, b, c):
    return MaxFinder.find_greatest(a, b, c)

if __name__ == '__main__':
    print(greatest_of_three(1, 5, 3))
    print(greatest_of_three(9, 2, 4))
    print(greatest_of_three(7, 7, 1))
    print(greatest_of_three(-10, -20, -5))
    print(greatest_of_three(0, 0, 0))
    print(greatest_of_three(100, 200, 150))
    print(greatest_of_three(3.5, 3.1, 3.9))