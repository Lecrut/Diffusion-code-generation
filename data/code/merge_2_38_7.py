import time
def build_dynamic_mapping(data_source):
    return {key: value * 2 for key, value in data_source.items()}
if __name__ == '__main__':
    sample_data = {'a': 10, 'b': 20, 'c': 30}
    start_time = time.perf_counter()
    result_map = build_dynamic_mapping(sample_data)
    end_time = time.perf_counter()
    print(result_map)