class ListSearcher:
    @staticmethod
    def find_target(data, target):
        return {"found": target in data, "index": data.index(target) if target in data else None}

if __name__ == '__main__':
    searcher = ListSearcher()
    sample_list = [10, 25, 3, 42, 15, 7]
    target_value = 42
    result1 = searcher.find_target(sample_list, target_value)
    print(f"List: {sample_list}, Target: {target_value}")
    print(result1)
    sample_list_2 = [1, 5, 9, 12, 3]
    target_value_2 = 100
    result2 = searcher.find_target(sample_list_2, target_value_2)
    print(f"List: {sample_list_2}, Target: {target_value_2}")
    print(result2)
    sample_list_3 = [5, 10, 15, 20]
    target_value_3 = 15
    result3 = searcher.find_target(sample_list_3, target_value_3)
    print(f"List: {sample_list_3}, Target: {target_value_3}")
    print(result3)