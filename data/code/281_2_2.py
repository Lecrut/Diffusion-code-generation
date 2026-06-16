class ValueSummer:
    def __init__(self, values):
        self.values = values
    def sum_values(self):
        return sum(self.values)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    summer = ValueSummer(sample_list)
    result = summer.sum_values()
    print(result)