class MaxFinder:
    @staticmethod
    def find_largest(a, b, c):
        return max(a, b, c)

if __name__ == '__main__':
    largest = MaxFinder.find_largest(3.5, 2.1, 4.8)
    print(f"The largest number is: {largest}")