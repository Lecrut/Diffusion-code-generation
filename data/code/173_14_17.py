class RemainderGrouper:
    def __init__(self):
        self.grouped = {}

    def group_by_remainder(self, numbers):
        for num in numbers:
            remainder = num % 3
            if remainder not in self.grouped:
                self.grouped[remainder] = []
            self.grouped[remainder].append(num)

    @staticmethod
    def get_sample_values():
        return [10, 23, 45, 68, 90, 12]

if __name__ == '__main__':
    grouper = RemainderGrouper()
    sample_values = RemainderGrouper.get_sample_values()
    grouper.group_by_remainder(sample_values)
    print(grouper.grouped)