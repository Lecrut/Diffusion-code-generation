class SafeListAccess:
    def __init__(self, elements):
        self.elements = elements

    @classmethod
    def safe_access(cls, instance, position):
        if 0 <= position < len(instance.elements):
            return instance.elements[position]
        else:
            return None

if __name__ == '__main__':
    sample_values = [201, 301, 401, 501, 601]
    safe_instance = SafeListAccess(sample_values)
    
    index_to_check = 2
    result = SafeListAccess.safe_access(safe_instance, index_to_check)
    print(f"Element at index {index_to_check}: {result}")
    
    invalid_index = 7
    result_invalid = SafeListAccess.safe_access(safe_instance, invalid_index)
    print(f"Element at invalid index {invalid_index}: {result_invalid}")