class SafeListAccess:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        try:
            return instance.elements[position]
        except IndexError:
            return None

if __name__ == '__main__':
    SAMPLE_LIST = [10, 20, 30, 40, 50]
    POSITION_TO_ACCESS_1 = 2
    POSITION_TO_ACCESS_2 = 10

    safe_list_instance = SafeListAccess(SAMPLE_LIST)
    
    result_1 = SafeListAccess.safe_access(safe_list_instance, POSITION_TO_ACCESS_1)
    print(result_1)
    
    result_2 = SafeListAccess.safe_access(safe_list_instance, POSITION_TO_ACCESS_2)
    print(result_2)