def contains_target(target, string_list):
    return target in string_list

if __name__ == '__main__':
    sample_target = "example"
    sample_list = ["apple", "banana", "cherry", "date"]
    print(contains_target(sample_target, sample_list))