store_names = ["Store X", "Store Y", "Store Z"]
ages = [15, 20, 35]

def create_store_dict(names, ages):
    return dict(zip(names, ages))

if __name__ == '__main__':
    store_ages = create_store_dict(store_names, ages)
    print(store_ages)