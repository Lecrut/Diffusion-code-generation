class ListSearcher:
    @staticmethod
    def find_last_occurrence(data, element):
        if not data:
            return -1
        for index in range(len(data) - 1, -1, -1):
            if data[index] == element:
                return index
        return -1

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 30]
    target_element = 30
    searcher = ListSearcher()
    result = searcher.find_last_occurrence(sample_data, target_element)
    print(result)

    empty_data = []
    empty_result = searcher.find_last_occurrence(empty_data, target_element)
    print(empty_result)

    single_data = [99]
    single_result = searcher.find_last_occurrence(single_data, 99)
    print(single_result)

    not_found_data = [10, 20, 30, 40, 50]
    not_found_result = searcher.find_last_occurrence(not_found_data, 60)
    print(not_found_result)