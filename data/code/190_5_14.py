def is_object_in_list(target_list, target_object):
    return any(id(obj) == id(target_object) for obj in target_list)

if __name__ == '__main__':
    sample_objects = [1, "hello", 3.14, True]
    empty_list = []
    object_to_find = "hello"
    non_existent_object = 99

    print(f"Checking if {object_to_find} is in {sample_objects}: {is_object_in_list(sample_objects, object_to_find)}")
    print(f"Checking if {non_existent_object} is in {sample_objects}: {is_object_in_list(sample_objects, non_existent_object)}")
    print(f"Checking if an empty list contains anything: {is_object_in_list(empty_list, 5)}")