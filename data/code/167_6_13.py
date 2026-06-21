STORE_NAMES = ["Store A", "Store B", "Store C"]
AGES = [5, 3, 8]

def create_store_dict(names=STORE_NAMES, ages=AGES):
    return dict(zip(names, ages))

if __name__ == '__main__':
    store_ages = create_store_dict()
    print(store_ages)