class FruitColorStore:
    FRUIT_COLORS = {'orange': 'orange', 'grape': 'purple'}

    @staticmethod
    def get_color(fruit):
        return FruitColorStore.FRUIT_COLORS.get(fruit, None)

if __name__ == '__main__':
    fc_store = FruitColorStore()
    print(fc_store.get_color('orange'))
    print(fc_store.get_color('grape'))