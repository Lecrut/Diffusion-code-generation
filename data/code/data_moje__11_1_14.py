class ListPoper:
    @staticmethod
    def pop_last_safe(data_list):
        if not data_list:
            return None
        return data_list.pop()

if __name__ == '__main__':
    numbers = [5, 15, 25, 35]
    popped_value = ListPoper.pop_last_safe(numbers)
    print(popped_value)
    print(numbers)
    empty_collection = []
    none_value = ListPoper.pop_last_safe(empty_collection)
    print(none_value)
    print(empty_collection)