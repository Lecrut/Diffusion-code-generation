def is_object_in_list(target, obj_list):
    return target in obj_list

if __name__ == '__main__':
    sample_obj = "example"
    sample_list = ["apple", "banana", "cherry", "example"]
    print(is_object_in_list(sample_obj, sample_list))