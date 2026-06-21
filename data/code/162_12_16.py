categories = ('Fruit', 'Vegetable', 'Beverage')
category_map = {category: index for index, category in enumerate(categories)}
if __name__ == '__main__':
    print(category_map['Fruit'])
    print(category_map['Vegetable'])
    print(category_map['Beverage'])