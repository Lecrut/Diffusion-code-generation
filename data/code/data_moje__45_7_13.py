def find_minimum(numbers):
    if not numbers:
        raise ValueError("List is empty")
    if len(numbers) == 1:
        return numbers[0]
    min_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    print(find_minimum(sample_list))
    single_element_list = [42]
    print(find_minimum(single_element_list))
    negative_list = [-5, -1, -3]
    print(find_minimum(negative_list))