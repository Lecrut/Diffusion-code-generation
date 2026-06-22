class MaxFinder:
    @staticmethod
    def find_max(a, b, c):
        return max(a, b, c)

if __name__ == '__main__':
    a = 10
    b = 25
    c = 10
    print(f"The largest number between {a}, {b}, and {c} is: {MaxFinder.find_max(a, b, c)}")