import random
def check_number_existence(numbers, target):
    return target in numbers
if __name__ == '__main__':
    sample_list = [1, 5, 10, 42, 7, 99]
    target_number = 42
    exists = check_number_existence(sample_list, target_number)
    print(f"The list of numbers is: {sample_list}")
    print(f"The target number to check for is: {target_number}")
    if exists:
        print(f"{target_number} exists in the list.")
    else:
        print(f"{target_number} does not exist in the list.")