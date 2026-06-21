def contains_target(strings, target):
    return target in strings

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry"]
    target_string = "banana"
    print(contains_target(sample_strings, target_string))