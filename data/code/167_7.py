class StoreDataHandler:
    def __init__(self):
        self.data = {}
    def add_store_data(self, store_name, age):
        self.data[store_name] = age
    def get_store_age(self, store_name):
        return self.data.get(store_name)
if __name__ == '__main__':
    handler = StoreDataHandler()
    handler.add_store_data("StoreA", 10)
    handler.add_store_data("StoreB", 25)
    handler.add_store_data("StoreC", 30)
    print(f"Age of StoreA: {handler.get_store_age('StoreA')}")
    print(f"Age of StoreB: {handler.get_store_age('StoreB')}")
    print(f"Age of StoreC: {handler.get_store_age('StoreC')}")
    print(f"Age of StoreD: {handler.get_store_age('StoreD')}")