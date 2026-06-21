class TupleProductCalculator:
    @staticmethod
    def calculate_product(data):
        product = 1
        for item in data:
            product *= item[0]
        return product

if __name__ == '__main__':
    sample_data = [(2, 3), (4, 5), (6, 7)]
    result = TupleProductCalculator.calculate_product(sample_data)
    print(result)