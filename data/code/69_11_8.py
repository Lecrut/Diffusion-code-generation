class StringAccessor:
    def __init__(self, data):
        self.data = data

    def get_characters(self, indices):
        result = []
        for index in indices:
            if 0 <= index < len(self.data):
                result.append(self.data[index])
            else:
                result.append(None)
        return result

if __name__ == '__main__':
    sample_string = "hello world"
    sample_indices_valid = [0, 2, 4]
    sample_indices_invalid = [1, 5, -1, 3]
    
    accessor = StringAccessor(sample_string)
    
    result_valid = accessor.get_characters(sample_indices_valid)
    print(f"String: {sample_string}")
    print(f"Indices (Valid): {sample_indices_valid}")
    print(f"Result (Valid Indices): {result_valid}")
    
    result_invalid = accessor.get_characters(sample_indices_invalid)
    print(f"Indices (Invalid): {sample_indices_invalid}")
    print(f"Result (Invalid Indices): {result_invalid}")