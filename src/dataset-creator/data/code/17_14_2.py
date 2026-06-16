import timeit
def check_containment(obj_list):
    return any(item in [10, 20] for item in obj_list)
if __name__ == '__main__':
    sample_objects = ['a', 'b']
    target_collection = {5, 6}
    start_time = timeit.default_timer()
    result_list = check_containment(sample_objects)
    end_time = timeit.default_timer()
    print(f"Result: {result_list}")