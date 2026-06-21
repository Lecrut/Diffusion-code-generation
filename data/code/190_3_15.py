def check_membership(iterable, value):
    return value in iterable

if __name__ == '__main__':
    sample_list = [1.5, 2.5, 3.5]
    target_value = 2.5
    result = check_membership(sample_list, target_value)
    print(f"Is {target_value} in {sample_list}? {result}")