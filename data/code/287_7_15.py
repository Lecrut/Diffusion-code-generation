class ShoppingCart:
    WEIGHT_CONVERSION_FACTOR = 1000

    @staticmethod
    def calculate_total_weight(cart):
        total_weight_grams = sum(item[1] for item in cart)
        return total_weight_grams / ShoppingCart.WEIGHT_CONVERSION_FACTOR

if __name__ == '__main__':
    shopping_cart = [
        ("apple", 200),
        ("banana", 150),
        ("orange", 300)
    ]
    print(ShoppingCart.calculate_total_weight(shopping_cart))