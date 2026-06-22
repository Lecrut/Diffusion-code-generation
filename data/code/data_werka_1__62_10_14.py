def get_second_item(lst):
    if len(lst) < 2:
        return None
    return lst[1]

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30]
    sample_list_2 = ['a', 'b']
    sample_list_3 = [5]
    
    second_item_1 = get_second_item(sample_list_1)
    second_item_2 = get_second_item(sample_list_2)
    second_item_3 = get_second_item(sample_list_3)
    
    print("The second item in sample_list_1 is:", second_item_1)
    print("The second item in sample_list_2 is:", second_item_2)
    print("The second item in sample_list_3 is:", second_item_3)