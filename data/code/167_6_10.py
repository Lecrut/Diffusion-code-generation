store_names = ['Store A', 'Store B', 'Store C']
ages = [10, 20, 30]

def zip_stores_and_ages(names, ages):
    return dict(zip(names, ages))

if __name__ == '__main__':
    result = zip_stores_and_ages(store_names, ages)
    print(result)