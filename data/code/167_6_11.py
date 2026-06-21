class StoreAgeMapper:
    def __init__(self):
        self.store_names = ["Store A", "Store B", "Store C"]
        self.ages = [5, 3, 8]

    def create_store_dict(self):
        return dict(zip(self.store_names, self.ages))

if __name__ == '__main__':
    mapper = StoreAgeMapper()
    store_dict = mapper.create_store_dict()
    print(store_dict)