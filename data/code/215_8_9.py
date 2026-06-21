class MaxFinder:
    @staticmethod
    def find_maximum(a, b, c):
        return max(a, b, c)

if __name__ == '__main__':
    result = MaxFinder.find_maximum(10, 20, 30)
    print(f"Maximum of (10, 20, 30): {result}")