class FruitColorMapper:

    def __init__(self):
        self.fruit_colors = {'apple': 'red', 'banana': 'yellow'}

    def get_color(self, fruit):
        return self.fruit_colors.get(fruit, 'Unknown color')
if __name__ == '__main__':
    mapper = FruitColorMapper()
    print(mapper.get_color('apple'))
    print(mapper.get_color('banana'))
    print(mapper.get_color('cherry'))