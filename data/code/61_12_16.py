class SafeListHandler:
    def __init__(self, data_list):
        self.data_list = data_list

    @classmethod
    def fetch_element(cls, instance, index):
        try:
            return instance.data_list[index]
        except IndexError:
            return None

if __name__ == '__main__':
    example_data = [1000, 2000, 3000, 4000, 5000]
    handler_instance = SafeListHandler(example_data)
    
    index_to_fetch = 2
    fetched_element = SafeListHandler.fetch_element(handler_instance, index_to_fetch)
    print(f"Fetched element at index {index_to_fetch}: {fetched_element}")
    
    invalid_index = 10
    result_for_invalid_index = SafeListHandler.fetch_element(handler_instance, invalid_index)
    print(f"Attempt to fetch element at invalid index {invalid_index}: {result_for_invalid_index}")