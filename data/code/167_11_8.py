STORE_NAME = "Example Store"
STORE_AGE = 5

def get_store_info():
    return {'store_name': STORE_NAME, 'store_age': STORE_AGE}

if __name__ == '__main__':
    store_info = get_store_info()
    print(store_info)