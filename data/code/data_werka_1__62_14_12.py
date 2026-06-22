def get_second_item(data):
    MIN_LENGTH = 2
    if len(data) >= MIN_LENGTH:
        return data[1]
    else:
        return None

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5]
    sample_list_3 = []
    sample_list_4 = [100]
    
    print(f"List {sample_list_1}: {get_second_item(sample_list_1)}")
    print(f"List {sample_list_2}: {get_second_item(sample_list_2)}")
    print(f"List {sample_list_3}: {get_second_item(sample_list_3)}")
    print(f"List {sample_list_4}: {get_second_item(sample_list_4)}")