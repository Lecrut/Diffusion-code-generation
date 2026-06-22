import heapq

class SalaryAnalyzer:
    def __init__(self, salaries):
        self.salaries = salaries

    def find_max(self):
        if not self.salaries:
            return 0
        return heapq.nlargest(1, self.salaries)[0]

if __name__ == '__main__':
    raw_data = [3200, 8900, 15000, 4200, 21000, 9500, 18500, 7600, 33000, 12000]
    analyzer = SalaryAnalyzer(raw_data)
    print(analyzer.find_max())