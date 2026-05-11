import timeit
def efficient_mapping(input_dict, mapping_function):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[mapping_function(value)] = key
    return output_dict
if __name__ == '__main__':
    sample_input = {
        "a": 10,
        "b": 25,
        "c": 5,
        "d": 40
    }
    def add_ten(x):
        return x + 10
    start_time = timeit.default_timer()
    result = efficient_mapping(sample_input, add_ten)
    end_time = timeit.default_timer()
    print(f"Input Dictionary: {sample_input}")
    print(f"Mapping Function: add_ten")
    print(f"Result Dictionary: {result}")
    print(f"Execution Time: {(end_time - start_time):.6f} seconds")