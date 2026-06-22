class MedianFinder:
    @staticmethod
    def median_of_three(a, b, c):
        return sorted([a, b, c])[1]

if __name__ == '__main__':
    finder = MedianFinder()
    print(finder.median_of_three(5, 2, 8))
    print(finder.median_of_three(5, 1, 9))