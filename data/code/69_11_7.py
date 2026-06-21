def access_string_characters(s, indices):
    result = []
    for index in indices:
        try:
            if 0 <= index < len(s):
                result.append(s[index])
            else:
                raise IndexError("Index out of bounds")
        except IndexError as e:
            result.append(str(e))
    return result

if __name__ == '__main__':
    sample_string = "Hello, World!"
    sample_indices_valid = [0, 7, 12]
    sample_indices_invalid = [-1, 13, 5]
    
    result_valid = access_string_characters(sample_string, sample_indices_valid)
    print(f"String: {sample_string}")
    print(f"Valid Indices: {sample_indices_valid}")
    print(f"Result (Valid): {result_valid}")
    
    result_invalid = access_string_characters(sample_string, sample_indices_invalid)
    print(f"Invalid Indices: {sample_indices_invalid}")
    print(f"Result (Invalid): {result_invalid}")