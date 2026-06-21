categories = ('Fruit', 'Vegetable', 'Beverage')
category_codes = {category: index for index, category in enumerate(categories)}

def get_category_code(category):
    return category_codes.get(category, -1)
if __name__ == '__main__':
    print(get_category_code('Fruit'))
    print(get_category_code('Vegetable'))
    print(get_category_code('Beverage'))
    print(get_category_code('Meat'))