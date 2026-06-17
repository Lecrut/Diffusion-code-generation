class MedianFinder:
    def get_middle(self, a, b, c):
        nums = sorted([a, b, c])
        return nums[1]
if __name__ == '__main__':
    mf = MedianFinder()
    print(mf.get_middle(1, 5, 2))
    print(mf.get_middle(10, 20, 30))
    print(mf.get_middle(7, 7, 7))
    print(mf.get_middle(1, 100, 50))