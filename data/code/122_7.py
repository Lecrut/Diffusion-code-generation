class ListAverager:
    def __init__(self, data):
        self.data = data
    def calculate_average(self):
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    averager = ListAverager(sample_list)
    average = averager.calculate_average()
    print(average)