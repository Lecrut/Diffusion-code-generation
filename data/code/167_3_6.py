stores = ['Store A', 'Store B', 'Store C']
ages = {store: 10 + i for i, store in enumerate(stores)}

if __name__ == '__main__':
    print(ages)