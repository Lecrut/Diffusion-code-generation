def find_min(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_list = [10, 5, 8, 3, 20]
    print(find_min(sample_list))
    single_element_list = [42]
    print(find_min(single_element_list))