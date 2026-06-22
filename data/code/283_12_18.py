class DuplicateDetector:
    def __init__(self):
        self.seen = set()

    @staticmethod
    def find_first_duplicate(lst):
        detector = DuplicateDetector()
        for item in lst:
            if item in detector.seen:
                return item
            detector.seen.add(item)
        return None

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2]
    print(DuplicateDetector.find_first_duplicate(sample_list))