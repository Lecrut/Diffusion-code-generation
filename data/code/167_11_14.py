def get_store_info():
    store_data = {
        'store_name': 'Example Store',
        'store_age': 5
    }
    return store_data

if __name__ == '__main__':
    store_info = get_store_info()
    print(store_info)