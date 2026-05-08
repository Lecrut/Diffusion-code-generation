if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    numbers_list = []
    all_valid = True
    for item in sample_numbers:
        if isinstance(item, (int, float)):
            numbers_list.append(item)
        else:
            all_valid = False
            break
    if all_valid and numbers_list:
        average = sum(numbers_list) / len(numbers_list)
        print(average)
    else:
        print("Error: One or more inputs were not valid numbers.")