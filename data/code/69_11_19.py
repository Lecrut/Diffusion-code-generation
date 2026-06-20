class StringIndexer:
    @staticmethod
    def access_string_characters(input_string, indices):
        result = []
        for index in indices:
            if 0 <= index < len(input_string):
                result.append(input_string[index])
            else:
                result.append(None)
        return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices_valid = [0, 4, 7]
    sample_indices_invalid = [-1, 12, 50]
    result_valid = StringIndexer.access_string_characters(sample_string, sample_indices_valid)
    print(f"String: {sample_string}")
    print(f"Indices (Valid): {sample_indices_valid}")
    print(f"Result (Valid Indices): {result_valid}")
    result_invalid = StringIndexer.access_string_characters(sample_string, sample_indices_invalid)
    print(f"Indices (Invalid): {sample_indices_invalid}")
    print(f"Result (Invalid Indices): {result_invalid}")