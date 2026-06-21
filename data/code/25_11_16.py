class DiscountCalculator:
    _PRICE_LIST = {
        'basic': 100.0,
        'standard': 200.0,
        'premium': 500.0,
    }

    _DISCOUNT_TIERS = [
        (5000, 0.10),
        (2000, 0.05),
        (0, 0.0),
    ]

    @staticmethod
    def get_base_price(item_code):
        if item_code in DiscountCalculator._PRICE_LIST:
            return DiscountCalculator._PRICE_LIST[item_code]
        return 0.0

    @staticmethod
    def calculate_final_price(item_code, quantity):
        base_price = DiscountCalculator.get_base_price(item_code)
        if base_price == 0.0 or quantity <= 0:
            return 0.0

        subtotal = base_price * quantity
        
        if subtotal >= 5000:
            discount_rate = 0.10
        elif subtotal >= 2000:
            discount_rate = 0.05
        else:
            discount_rate = 0.0

        discount_amount = subtotal * discount_rate
        final_price = subtotal - discount_amount
        return final_price

if __name__ == '__main__':
    calc = DiscountCalculator()
    item = 'premium'
    qty = 15
    price = DiscountCalculator.calculate_final_price(item, qty)
    print(price)