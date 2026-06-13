def check_number_in_list(numbers, target):
    return target in numbers
if __name__ == '__main__':
    sample_numbers = [10, 25, 37, 42, 50]
    target_number = 37
    result = check_number_in_list(sample_numbers, target_number)
    print(f"The list is: {sample_numbers}")
    print(f"The target number is: {target_number}")
    if result:
        print("Target number found in the list.")
    else:
        print("Target number not found in the list.")