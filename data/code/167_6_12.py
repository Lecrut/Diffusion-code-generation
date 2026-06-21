def generate_store_info():
    store_names = ['Store A', 'Store B', 'Store C']
    ages = [20, 30, 40]
    return dict(zip(store_names, ages))

if __name__ == '__main__':
    store_info = generate_store_info()
    print(store_info)