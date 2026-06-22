class MaxFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data)

if __name__ == '__main__':
    finder = MaxFinder()
    print(f"Largest in [1, 5, 2, 8, 3]: {finder.find_largest([1, 5, 2, 8, 3])}")
    print(f"Largest in [-10, -5, -20]: {finder.find_largest([-10, -5, -20])}")
    print(f"Largest in [42]: {finder.find_largest([42])}")
    try:
        finder.find_largest([])
    except ValueError as e:
        print(e)