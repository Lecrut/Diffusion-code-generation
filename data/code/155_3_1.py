class ListSummer:
    def get_total_sum(self, data_list):
        total = 0
        for item in data_list:
            total += item
        return total
if __name__ == '__main__':
    summer = ListSummer()
    sample_list = [1, 5, 10, 2]
    result = summer.get_total_sum(sample_list)
    print(result)