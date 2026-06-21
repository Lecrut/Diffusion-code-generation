categories = ('CategoryA', 'CategoryB', 'CategoryC')
category_codes = {category: index for index, category in enumerate(categories)}

def get_category_code(category):
    return category_codes.get(category, None)
if __name__ == '__main__':
    print(get_category_code('CategoryA'))
    print(get_category_code('CategoryB'))
    print(get_category_code('CategoryC'))
    print(get_category_code('CategoryD'))