class DetermineTheLargestNumberPresentManager:
    DEFAULT_ENTRIES = [10, 5, 20, 3, 15]

    @staticmethod
    def find_largest_number(entries):
        return max(entries)

if __name__ == '__main__':
    manager = DetermineTheLargestNumberPresentManager()
    largest_number = DetermineTheLargestNumberPresentManager.find_largest_number(manager.DEFAULT_ENTRIES)
    print(largest_number)