def all_even(input_list):
    return all(x % 2 == 0 for x in input_list)

if __name__ == '__main__':
    list1 = [2, 4, 6, 8]
    list2 = [1, 3, 5, 7]
    list3 = []
    print(f"All elements in list1 are even: {all_even(list1)}")
    print(f"All elements in list2 are even: {all_even(list2)}")
    print(f"All elements in list3 are even: {all_even(list3)}")