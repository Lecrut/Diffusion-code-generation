def get_first_element(numbers):
    if len(numbers) == 0:
        return None
    return numbers[0]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = []
    sample_list_3 = [5]
    
    result_1 = get_first_element(sample_list_1)
    result_2 = get_first_element(sample_list_2)
    result_3 = get_first_element(sample_list_3)
    
    print(result_1)
    print(result_2)
    print(result_3)