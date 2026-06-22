class MedianFinder:
    def find_median(self, a, b, c):
        if (a - b) * (c - a) >= 0:
            return a
        elif (b - a) * (c - b) >= 0:
            return b
        else:
            return c

if __name__ == '__main__':
    finder = MedianFinder()
    median1 = finder.find_median(5, 2, 8)
    median2 = finder.find_median(5, 1, 9)
    print(median1)
    print(median2)