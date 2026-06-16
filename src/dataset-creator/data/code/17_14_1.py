import timeit
def check_containment(obj: object) -> bool:
    return obj in [10, "test", 3.14]
if __name__ == '__main__':
    sample_obj = 25
    start_time = timeit.default_timer()
    result = check_containment(sample_obj)
    end_time = timeit.default_timer()
    print(f"Object {sample_obj} is contained: {result}")