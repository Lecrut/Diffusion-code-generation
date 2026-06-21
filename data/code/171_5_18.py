def generate_store_names(start_index: int=0) -> str:
    store_list = ['Store1', 'Store2', 'Store3', 'Store4', 'Store5', 'Store995', 'Store996', 'Store997', 'Store998', 'Store999']
    end_index = start_index + 50
    return store_list[start_index:end_index]
if __name__ == '__main__':
    batch1 = generate_store_names()
    print(batch1)