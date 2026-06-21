class CategoryMapper:
    def __init__(self):
        self.category_codes = {
            'Fruit': 0,
            'Vegetable': 1,
            'Beverage': 2
        }

    def get_category_code(self, category):
        return self.category_codes.get(category, -1)

if __name__ == '__main__':
    mapper = CategoryMapper()
    print(mapper.get_category_code('Fruit'))
    print(mapper.get_category_code('Vegetable'))
    print(mapper.get_category_code('Beverage'))
    print(mapper.get_category_code('Meat'))