class FruitColor:

    def __init__(self):
        self.fruit_color_map = {'orange': 'orange', 'grape': 'purple'}

    def get_color(self, fruit):
        return self.fruit_color_map.get(fruit, None)
if __name__ == '__main__':
    fc = FruitColor()
    print(fc.get_color('orange'))
    print(fc.get_color('grape'))