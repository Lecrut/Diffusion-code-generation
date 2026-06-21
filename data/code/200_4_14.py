class TupleProductCalculator:
    @staticmethod
    def calculate_product(tuples):
        product = 1
        for first_element, _ in tuples:
            product *= first_element
        return product

if __name__ == '__main__':
    sample_data = [(2, 'a'), (3, 'b'), (4, 'c')]
    result = TupleProductCalculator.calculate_product(sample_data)
    print(result)