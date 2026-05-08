def find_even_numbers(data):
    even_numbers = []
    for number in data:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5, 6]
    sample_list_2 = [1, 3, 5, 7, 9]
    sample_list_3 = [10, 20, 30, 40]
    sample_list_4 = []
    sample_list_5 = [2, 4, 6, 8, 10]
    result_1 = find_even_numbers(sample_list_1)
    print(f"List: {sample_list_1}, Even numbers: {result_1}")
    result_2 = find_even_numbers(sample_list_2)
    print(f"List: {sample_list_2}, Even numbers: {result_2}")
    result_3 = find_even_numbers(sample_list_3)
    print(f"List: {sample_list_3}, Even numbers: {result_3}")
    result_4 = find_even_numbers(sample_list_4)
    print(f"List: {sample_list_4}, Even numbers: {result_4}")
    result_5 = find_even_numbers(sample_list_5)
    print(f"List: {sample_list_5}, Even numbers: {result_5}")