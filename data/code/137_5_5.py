class MaxFinder:
    @staticmethod
    def get_max(a, b):
        return a if a > b else b

if __name__ == '__main__':
    print(MaxFinder.get_max(5, 3))