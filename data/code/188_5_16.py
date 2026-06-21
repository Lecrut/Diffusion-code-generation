def reverse_recursive(lst):
    if len(lst) <= 1:
        return lst
    else:
        return [lst[-1]] + reverse_recursive(lst[:-1])

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    print("Original list:", sample_list)
    print("Reversed list:", reverse_recursive(sample_list))
    another_list = ['e', 'd', 'c', 'b', 'a']
    print("Original list:", another_list)
    print("Reversed list:", reverse_recursive(another_list))