class MaxFinder:
    def find_max(self, a, b, c):
        return max(a, b, c)

if __name__ == '__main__':
    finder = MaxFinder()
    result = finder.find_max(10, 20, 30)
    print(result)