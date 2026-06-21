categories = ('Fruit', 'Vegetable', 'Beverage')
category_codes = {category: index for index, category in enumerate(categories)}

class CategoryMapper:
    CATEGORY_CODES = category_codes

    @staticmethod
    def get_category_code(category):
        return CategoryMapper.CATEGORY_CODES.get(category, -1)

if __name__ == '__main__':
    mapper = CategoryMapper()
    print(mapper.get_category_code('Fruit'))
    print(mapper.get_category_code('Vegetable'))
    print(mapper.get_category_code('Beverage'))
    print(mapper.get_category_code('Meat'))