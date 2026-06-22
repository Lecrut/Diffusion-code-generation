class MaxSquaredFinder:
    def find_max(self):
        return max(x**2 for x in range(1, 101))

if __name__ == '__main__':
    finder = MaxSquaredFinder()
    print(finder.find_max())