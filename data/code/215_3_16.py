class MaxFinder:
    def find_max(self):
        return max({4, 8, 15, 16, 23, 42})

if __name__ == '__main__':
    finder = MaxFinder()
    print(f"Maximum element: {finder.find_max()}")