class TieredDiscountCalculator:
    price_list = {
        'item_a': 100.0,
        'item_b': 50.0,
        'item_c': 25.0
    }
    
    tiers = [
        (5, 0.0),
        (10, 0.1),
        (20, 0.2),
        (float('inf'), 0.3)
    ]

    @staticmethod
    def calculate_discount(quantity):
        for limit, discount_rate in TieredDiscountCalculator.tiers:
            if quantity < limit:
                return discount_rate
        return 0.0

    @staticmethod
    def get_unit_price(item_name):
        return TieredDiscountCalculator.price_list.get(item_name, 0.0)

    @staticmethod
    def calculate_total(item_name, quantity):
        unit_price = TieredDiscountCalculator.get_unit_price(item_name)
        subtotal = unit_price * quantity
        discount_rate = TieredDiscountCalculator.calculate_discount(quantity)
        discount_amount = subtotal * discount_rate
        final_price = subtotal - discount_amount
        return {
            'item': item_name,
            'quantity': quantity,
            'unit_price': unit_price,
            'subtotal': subtotal,
            'discount_rate': discount_rate,
            'discount_amount': discount_amount,
            'final_price': final_price
        }

if __name__ == '__main__':
    result = TieredDiscountCalculator.calculate_total('item_a', 15)
    print(result)