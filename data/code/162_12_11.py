categories = ('Fruits', 'Vegetables', 'Beverages')
category_codes = {category: idx for idx, category in enumerate(categories)}

def get_category_code(category):
    return category_codes.get(category, None)
if __name__ == '__main__':
    sample_category = 'Vegetables'
    print(get_category_code(sample_category))