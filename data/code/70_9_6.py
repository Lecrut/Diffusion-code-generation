class ListChecker:
    def __init__(self, items):
        self.items = list(items)

    def get_first_and_last(self):
        count = len(self.items)
        if count == 0:
            raise ValueError("Cannot retrieve elements from an empty list")
        if count == 1:
            single_item = self.items[0]
            return single_item, single_item
        start_index = 0
        end_index = count - 1
        first_val = self.items[start_index]
        last_val = self.items[end_index]
        return first_val, last_val

if __name__ == '__main__':
    sample_data = [42, 99, 15, 7, 88]
    checker_instance = ListChecker(sample_data)
    output = checker_instance.get_first_and_last()
    print(output)