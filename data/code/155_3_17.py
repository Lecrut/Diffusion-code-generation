class ListSummer:
    def calculate_sum(self, data_list):
        return sum(x for x in data_list)

if __name__ == '__main__':
    summer = ListSummer()
    sample_list = [1, 2, 3, 4, 5]
    result = summer.calculate_sum(sample_list)
    print(result)