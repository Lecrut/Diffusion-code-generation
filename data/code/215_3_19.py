class MaxFinder:
    def get_max(self):
        return max({4, 8, 15, 16, 23, 42})

if __name__ == '__main__':
    finder = MaxFinder()
    print(f"Max element: {finder.get_max()}")