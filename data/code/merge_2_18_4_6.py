import json
def reverse_nested_sequence(data):
    if isinstance(data, list):
        return [reverse_nested_sequence(item) for item in reversed(data)]
    elif isinstance(data, tuple):
        return tuple(reversed(reverse_nested_sequence(list(data))))
    else:
        return data
def safe_reverse(input_data):
    try:
        if input_data is None:
            raise ValueError("Input cannot be None")
        if not hasattr(input_data, '__iter__') or isinstance(input_data, (str, bytes)):
            return "Error: Input must be an iterable sequence."
        result = reverse_nested_sequence(input_data)
        return result
    except Exception as e:
        return f"Unexpected error occurred during reversal: {str(e)}"
if __name__ == '__main__':
    sample_inputs = [
        [],
        None,
        "string",                                                                                               
        42,                  
        [[1, 2], [3, [4, 5]]],                    
        ((1,), (2, (3,))),                                     
        {"a": "b"},                                                                                                                                                                                                                                                                                                                         
        [1, 2],                                 
    ]
    test_cases = {
        "Empty List": [],
        "None Value": None,
        "Integer (Non-Sequence)": 42,
        "Nested Lists": [[1, 2], [3, [4, 5]]],
        "Tuples with Nested Tuples": ((1,), (2, (3,))),
        "Simple List": [1, 2]
    }
    for name, data in test_cases.items():
        output = safe_reverse(data)
        if isinstance(output, list):
            print(f"Input: {name}")
            print("Output:", output)
        elif isinstance(output, str):
            print(f"{output}\n")
    dict_test = {"key": "value"}
    print(f"Input (Dict): {dict_test}")
    result_dict = reverse_nested_sequence(dict_test) if isinstance(dict_test, list) else None                                                      
    final_output = safe_reverse([1, 2])
    print("Final Test Result:", final_output)