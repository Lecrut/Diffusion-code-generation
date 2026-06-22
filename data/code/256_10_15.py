def find_range(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return 0
    else:
        return max(numbers) - min(numbers)
if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_range(sample_values))
    empty_list = []
    print(find_range(empty_list))
    single_element = [42]
    print(find_range(single_element))