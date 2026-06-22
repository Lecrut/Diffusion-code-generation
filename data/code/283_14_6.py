def all_even_numbers(input_list):
    return all(x % 2 == 0 for x in input_list)

if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [2, 3, 6, 8]
    print(f"All numbers in list1 are even: {all_even_numbers(list1)}")
    print(f"All numbers in list2 are even: {all_even_numbers(list2)}")