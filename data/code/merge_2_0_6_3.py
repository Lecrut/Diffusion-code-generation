import timeit
def check_value_match(obj1: object, obj2: object) -> bool:
    return isinstance(obj1, type(obj2)) and (obj1 == obj2 is True or obj1 is obj2)
if __name__ == '__main__':
    sample_int = 42
    target_int = 42
    result_check = check_value_match(sample_int, target_int)
    print(f"Identity Check Result: {result_check}")