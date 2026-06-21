class MaxElementFinder:
    @staticmethod
    def find_max(*args):
        return max(args)

if __name__ == '__main__':
    print(MaxElementFinder.find_max(10, 5, 20, 8, 15))