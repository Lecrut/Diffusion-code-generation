class ProductMapper:
    PRODUCT_IDS = {
        'Apple': 1,
        'Banana': 2,
        'Cherry': 3,
        'Date': 4,
        'Elderberry': 5
    }

    @staticmethod
    def map_product_names_to_ids(product_names):
        return {name: ProductMapper.PRODUCT_IDS.get(name, None) for name in product_names}

if __name__ == '__main__':
    sample_products = ['Apple', 'Banana', 'Grape']
    mapper = ProductMapper()
    print(mapper.map_product_names_to_ids(sample_products))