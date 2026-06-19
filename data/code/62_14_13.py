def retrieve_second_item(data):
    if len(data) >= 2:
        return data[1]
    else:
        return None

if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5]
    sample_list_3 = []
    sample_list_4 = [100]

    print(f"Sample List 1: {retrieve_second_item(sample_list_1)}")
    print(f"Sample List 2: {retrieve_second_item(sample_list_2)}")
    print(f"Sample List 3: {retrieve_second_item(sample_list_3)}")
    print(f"Sample List 4: {retrieve_second_item(sample_list_4)}")