class SafeListContainer:
    ERROR_MESSAGE = "IndexError: List does not have a second element"
    
    def __init__(self, data):
        self._data = data
    
    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError:
            return SafeListContainer.ERROR_MESSAGE

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40]
    sample_list_b = [5]
    sample_list_c = []
    
    container_a = SafeListContainer(sample_list_a)
    container_b = SafeListContainer(sample_list_b)
    container_c = SafeListContainer(sample_list_c)
    
    print(f"Result for {sample_list_a}: {container_a.get_second_element()}")
    print(f"Result for {sample_list_b}: {container_b.get_second_element()}")
    print(f"Result for {sample_list_c}: {container_c.get_second_element()}")