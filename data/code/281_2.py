class ValueSummer:
    def __init__(self, values):
        self.values = values
    def sum_values(self):
        return sum(self.values)
if __name__ == '__main__':
    sample_list = [10, 25, 30, 5]
    summer = ValueSummer(sample_list)
    total = summer.sum_values()
    print(total)