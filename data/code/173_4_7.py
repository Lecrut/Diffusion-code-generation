import operator

def group_by_attribute(objects, attr):
    grouped = {}
    for obj in objects:
        key = getattr(obj, attr)
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(obj)
    return grouped

if __name__ == '__main__':
    class Product:
        def __init__(self, name, category):
            self.name = name
            self.category = category
    
    products = [
        Product("Laptop", "Electronics"),
        Product("Mouse", "Electronics"),
        Product("Blender", "Appliances"),
        Product("Microwave", "Appliances")
    ]
    
    grouped_products = group_by_attribute(products, 'category')
    for category, products_in_category in grouped_products.items():
        print(f"Category: {category}")
        for product in products_in_category:
            print(f"  - {product.name}")