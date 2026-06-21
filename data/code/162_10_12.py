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
    mapper = ProductMapper()
    sample_products = ['Apple', 'Banana', 'Grape']
    mapped_ids = mapper.map_product_names_to_ids(sample_products)
    print(mapped_ids)