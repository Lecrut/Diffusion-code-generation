category_names = ('Fruit', 'Vegetable', 'Beverage', 'Dairy')
category_constants = {name: index for index, name in enumerate(category_names)}

def get_category_constant(name):
    return category_constants.get(name, None)
if __name__ == '__main__':
    print(get_category_constant('Fruit'))
    print(get_category_constant('Vegetable'))
    print(get_category_constant('Beverage'))
    print(get_category_constant('Dairy'))
    print(get_category_constant('Meat'))