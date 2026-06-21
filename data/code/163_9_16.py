class FruitColorMerger:

    def __init__(self):
        self.fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple', 'orange': 'orange'}

    def merge_fruits_and_colors(self, additional_fruits, additional_colors):
        if len(additional_fruits) != len(additional_colors):
            raise ValueError('Fruit and color lists must be of the same length')
        for fruit, color in zip(additional_fruits, additional_colors):
            self.fruit_colors[fruit] = color

    def get_all_fruit_colors(self):
        return self.fruit_colors
if __name__ == '__main__':
    merger = FruitColorMerger()
    new_fruits = ['strawberry', 'kiwi']
    new_colors = ['red', 'green']
    merger.merge_fruits_and_colors(new_fruits, new_colors)
    print(merger.get_all_fruit_colors())