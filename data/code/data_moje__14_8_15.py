TARGET_INDEX = 2

def get_third_element(data_list):
    return data_list[TARGET_INDEX]

class ElementAccessor:
    def __init__(self, data):
        self.data = data
    
    def fetch(self):
        return self.data[TARGET_INDEX]

if __name__ == '__main__':
    test_values = [100, 200, 305, 400, 500]
    direct_result = get_third_element(test_values)
    print(direct_result)
    
    accessor = ElementAccessor(test_values)
    class_result = accessor.fetch()
    print(class_result)