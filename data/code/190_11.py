import random
def check_number_in_list(numbers, target):
    return target in numbers
if __name__ == '__main__':
    sample_list = [10, 25, 33, 42, 56, 78, 91]
    target_number = 42
    result = check_number_in_list(sample_list, target_number)
    if result:
        print(f"The number {target_number} exists in the list.")
    else:
        print(f"The number {target_number} does not exist in the list.")