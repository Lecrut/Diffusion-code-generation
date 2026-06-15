def check_number_in_list(numbers, target):
    return target in numbers
if __name__ == '__main__':
    sample_list = [10, 25, 33, 42, 51]
    target_number = 33
    result = check_number_in_list(sample_list, target_number)
    print(f"List: {sample_list}")
    print(f"Target: {target_number}")
    print(f"Is the target in the list? {result}")