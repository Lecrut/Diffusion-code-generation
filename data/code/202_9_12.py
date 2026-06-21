class MaxFinder:
    @staticmethod
    def find_max(a, b, c):
        if a >= b and a >= c:
            return a
        elif b >= a and b >= c:
            return b
        else:
            return c

if __name__ == '__main__':
    max_val = MaxFinder.find_max(10, 20, 30)
    print(max_val)