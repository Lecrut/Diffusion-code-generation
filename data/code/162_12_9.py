categories = ('Fruit', 'Vegetable', 'Beverage')
category_codes = {category: index for index, category in enumerate(categories)}

def get_category_code(category):
    return category_codes.get(category, -1)

if __name__ == '__main__':
    sample_categories = ('Fruit', 'Meat', 'Vegetable', 'Beverage')
    results = [get_category_code(category) for category in sample_categories]
    print(results)