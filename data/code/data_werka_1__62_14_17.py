def fetch_second_item(data):
    return data[1] if len(data) >= 2 else None

if __name__ == '__main__':
    sample_lists = {
        'list1': [10, 20, 30, 40],
        'list2': [5],
        'list3': [],
        'list4': [100]
    }
    
    for name, lst in sample_lists.items():
        print(f"{name}: {fetch_second_item(lst)}")