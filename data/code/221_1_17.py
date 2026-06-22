class MedianFinder:
    @staticmethod
    def find_median(a, b, c):
        if (a < b < c) or (c < b < a):
            return b
        elif (b < a < c) or (c < a < b):
            return a
        else:
            return c

if __name__ == '__main__':
    median = MedianFinder.find_median(5, 2, 8)
    print(median)