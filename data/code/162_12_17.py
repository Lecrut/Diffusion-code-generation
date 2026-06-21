categories = ('Electronics', 'Clothing', 'Home Appliances')
category_codes = {category: index for index, category in enumerate(categories)}

def get_category_code(category):
    return category_codes.get(category, -1)
if __name__ == '__main__':
    print(get_category_code('Electronics'))
    print(get_category_code('Clothing'))
    print(get_category_code('Home Appliances'))
    print(get_category_code('Books'))