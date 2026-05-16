if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    numbers_list = []
    valid_input = True
    for item in sample_numbers:
        try:
            numbers_list.append(float(item))
        except ValueError:
            valid_input = False
            break
    if valid_input and numbers_list:
        average = sum(numbers_list) / len(numbers_list)
        print(average)
    else:
        print("Error: One or more inputs were not valid numbers.")