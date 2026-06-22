class MultiplicationTableGenerator:
    TARGET_NUMBER = 6
    MAX_MULTIPLIER = 10

    @staticmethod
    def _compute_product(base, multiplier):
        return base * multiplier

    @classmethod
    def generate_table(cls):
        table_dict = {}
        for i in range(1, cls.MAX_MULTIPLIER + 1):
            product = cls._compute_product(cls.TARGET_NUMBER, i)
            table_dict[i] = product
        return table_dict

if __name__ == '__main__':
    result = MultiplicationTableGenerator.generate_table()
    print(result)