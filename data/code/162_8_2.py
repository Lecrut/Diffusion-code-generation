import timeit
def efficient_mapping(input_dict, mapping_func):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[mapping_func(key, value)] = value
    return output_dict
if __name__ == '__main__':
    input_data = {
        "apple": 1,
        "banana": 2,
        "cherry": 3,
        "date": 4,
        "elderberry": 5
    }
    def simple_map(k, v):
        return k.upper() + str(v)
    start_time = timeit.default_timer()
    result = efficient_mapping(input_data, simple_map)
    end_time = timeit.default_timer()
    print(f"Input Dictionary: {input_data}")
    print(f"Mapping Function: lambda k, v: k.upper() + str(v)")
    print(f"Result: {result}")
    print(f"Execution Time: {(end_time - start_time):.6f} seconds")