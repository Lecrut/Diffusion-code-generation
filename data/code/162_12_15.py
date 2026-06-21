class CategoryMapper:
    CATEGORIES = ('Fruit', 'Vegetable', 'Beverage')
    CATEGORY_CODES = {category: index for index, category in enumerate(CATEGORIES)}

    @staticmethod
    def get_category_code(category):
        return CategoryMapper.CATEGORY_CODES.get(category, -1)

if __name__ == '__main__':
    print(CategoryMapper.get_category_code('Fruit'))
    print(CategoryMapper.get_category_code('Vegetable'))
    print(CategoryMapper.get_category_code('Beverage'))
    print(CategoryMapper.get_category_code('Meat'))