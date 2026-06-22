class MedianFinder:

    def __init__(self):
        self.nums = []

    def add_num(self, num: int) -> None:
        self.nums.append(num)

    def find_median(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n == 0:
            return None
        elif n % 2 == 1:
            return self.nums[n // 2]
        else:
            mid1 = self.nums[n // 2 - 1]
            mid2 = self.nums[n // 2]
            return (mid1 + mid2) / 2.0
if __name__ == '__main__':
    mf = MedianFinder()
    mf.add_num(3)
    mf.add_num(1)
    print(mf.find_median())
    mf.add_num(4)
    print(mf.find_median())