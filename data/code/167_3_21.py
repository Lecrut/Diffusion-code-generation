class StoreAgeMapper:

    def __init__(self):
        self.store_ages = {'Bookstore': 25, 'Grocery Shop': 40, 'Electronics Store': 33, 'Bakery': 55}

    def get_age(self, store_name):
        return self.store_ages.get(store_name, None)
if __name__ == '__main__':
    mapper = StoreAgeMapper()
    print(mapper.get_age('Bookstore'))
    print(mapper.get_age('Electronics Store'))
    print(mapper.get_age('Toy Store'))