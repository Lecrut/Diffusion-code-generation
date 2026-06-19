class ListFinder:
    @staticmethod
    def find_last_index(data, value):
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        last_index = -1
        for i in range(len(data) - 1, -1, -1):
            if data[i] == value:
                last_index = i
                break
        return last_index

if __name__ == '__main__':
    try:
        sample_list_1 = [3, 7, 9, 7, 2, 7, 5]
        target_value_1 = 7
        result_1 = ListFinder.find_last_index(sample_list_1, target_value_1)
        print(result_1)

        sample_list_2 = [10, 20, 30, 40, 50]
        target_value_2 = 60
        result_2 = ListFinder.find_last_index(sample_list_2, target_value_2)
        print(result_2)

        sample_list_3 = []
        target_value_3 = 1
        result_3 = ListFinder.find_last_index(sample_list_3, target_value_3)
        print(result_3)

    except Exception as e:
        print(f"An error occurred: {e}")