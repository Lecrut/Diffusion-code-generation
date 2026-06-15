class MedianFinder:
    def get_middle(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers[1]
if __name__ == '__main__':
    mf = MedianFinder()
    print(mf.get_middle(1, 5, 2))
    print(mf.get_middle(10, 20, 30))
    print(mf.get_middle(7, 1, 4))