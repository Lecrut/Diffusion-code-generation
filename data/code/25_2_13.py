class ProductPricing:
    BASE_PRICE = 500
    DISCOUNT_PERCENT = 20

    def __init__(self, price, percent):
        self.price = price
        self.percent = percent

    def get_savings(self):
        return self.price * (self.percent / 100)

    def get_final_price(self):
        return self.price - self.get_savings()

    def process(self):
        savings = self.get_savings()
        final = self.get_final_price()
        return savings, final

if __name__ == '__main__':
    processor = ProductPricing(ProductPricing.BASE_PRICE, ProductPricing.DISCOUNT_PERCENT)
    saved, cost = processor.process()
    print(saved)
    print(cost)