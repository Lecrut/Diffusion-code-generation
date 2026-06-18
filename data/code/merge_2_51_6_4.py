def find_first_element(data):
    if not isinstance(data, (list, tuple)):
        try:
            data = list(data)
        except TypeError:
            raise TypeError("Input must be a sequence-like structure or explicitly supported type.")
    if len(data) == 0:
        return None
    first_item = data[0]
    return first_item
if __name__ == '__main__':
    sample_list = [42, 'alpha', None]
    sample_tuple = ('beta', 3.14)
    sample_set_input = {7, 8}                                       
    print(f"First in list: {find_first_element(sample_list)}") 
    print(f"First in tuple: {find_first_element(sample_tuple)}") 
    try:
        result_set = find_first_element(sample_set_input)
        print(f"First from set conversion: {result_set}")                                                                                                                                                                                                                 
    except Exception as e:
        print(f"Error with set input: {e}")