def reverse_list(iterable):
    return iterable[::-1]

if __name__ == '__main__':
    list1 = [5, 4, 3, 2, 1]
    reversed_list1 = reverse_list(list1)
    print(f"Original: {list1}, Reversed: {reversed_list1}")
    
    list2 = ['c', 'b', 'a']
    reversed_list2 = reverse_list(list2)
    print(f"Original: {list2}, Reversed: {reversed_list2}")
    
    empty_list = []
    reversed_empty_list = reverse_list(empty_list)
    print(f"Original: {empty_list}, Reversed: {reversed_empty_list}")
    
    list3 = [10, 20]
    reversed_list3 = reverse_list(list3)
    print(f"Original: {list3}, Reversed: {reversed_list3}")