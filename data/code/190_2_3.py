def check_target_in_list(numbers, target):
    return target in numbers
if __name__ == '__main__':
    sample_numbers = [10, 25, 33, 42, 50]
    target_number = 33
    result = check_target_in_list(sample_numbers, target_number)
    print(f"List: {sample_numbers}")
    print(f"Target: {target_number}")
    print(f"Is the target in the list? {result}")