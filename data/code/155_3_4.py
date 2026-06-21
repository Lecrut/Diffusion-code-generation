class ListSummer:
    def get_total_sum(self, data_list):
        return sum(x for x in data_list)

if __name__ == '__main__':
    summer = ListSummer()
    sample_list_1 = [1, 2, 3, 4, 5]
    result_1 = summer.get_total_sum(sample_list_1)
    print(result_1)
    sample_list_2 = [10, 20, 30, 40]
    result_2 = summer.get_total_sum(sample_list_2)
    print(result_2)
    sample_list_3 = [-1, 5, -3, 10]
    result_3 = summer.get_total_sum(sample_list_3)
    print(result_3)