def get_store_info():
    store_data = {
        'store_name': 'Central Market',
        'store_age': 20
    }
    return store_data

if __name__ == '__main__':
    store_info = get_store_info()
    print(store_info)