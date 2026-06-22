class DiscountCalculator:
    PRICE_LIST = {
        "widget": 10.0,
        "gadget": 25.0,
        "doohickey": 50.0,
        "thingamajig": 100.0
    }
    
    TIERS = [
        (1000, 0.20),
        (500, 0.10),
        (100, 0.05),
        (0, 0.0)
    ]
    
    @staticmethod
    def calculate_discount(product_name, quantity):
        if product_name not in DiscountCalculator.PRICE_LIST:
            raise ValueError(f"Unknown product: {product_name}")
        
        unit_price = DiscountCalculator.PRICE_LIST[product_name]
        total_cost = unit_price * quantity
        
        discount_rate = 0.0
        for threshold, rate in DiscountCalculator.TIERS:
            if total_cost >= threshold:
                discount_rate = rate
                break
        
        discount_amount = total_cost * discount_rate
        final_price = total_cost - discount_amount
        
        return {
            "product": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_before_discount": total_cost,
            "discount_rate": discount_rate,
            "discount_amount": discount_amount,
            "final_price": final_price
        }

if __name__ == '__main__':
    calculator = DiscountCalculator()
    
    result1 = DiscountCalculator.calculate_discount("widget", 50)
    print(result1)
    
    result2 = DiscountCalculator.calculate_discount("gadget", 20)
    print(result2)
    
    result3 = DiscountCalculator.calculate_discount("doohickey", 30)
    print(result3)
    
    result4 = DiscountCalculator.calculate_discount("thingamajig", 5)
    print(result4)