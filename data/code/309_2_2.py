class SetSummer:
    def __init__(self, numbers):
        self.numbers = numbers
    def sum_elements(self):
        return sum(self.numbers)
if __name__ == '__main__':
    sample_list = [10, 25, 5, 40]
    summer = SetSummer(sample_list)
    result = summer.sum_elements()
    print(result)