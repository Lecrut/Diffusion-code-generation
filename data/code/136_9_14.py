class NumberTransformer:
    def transform_numbers(self, numbers):
        return (x * 2 if x % 3 == 0 or x % 5 == 0 else x for x in numbers)

if __name__ == '__main__':
    transformer = NumberTransformer()
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    transformed_result = transformer.transform_numbers(sample_numbers)
    print(list(transformed_result))