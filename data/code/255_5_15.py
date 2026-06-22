import random

class MaxFinder:
    MAX_NUM_GENERATED = 1000
    MIN_VALUE = 1
    MAX_VALUE = 100

    @staticmethod
    def generate_random_list(size=MAX_NUM_GENERATED, min_val=MIN_VALUE, max_val=MAX_VALUE):
        return [random.randint(min_val, max_val) for _ in range(size)]

    @staticmethod
    def find_max_value(data):
        if not data:
            raise ValueError("Data list is empty")
        max_value = data[0]
        for element in data[1:]:
            if element > max_value:
                max_value = element
        return max_value

if __name__ == '__main__':
    sample_list = MaxFinder.generate_random_list()
    print("Original List:", sample_list)
    max_val = MaxFinder.find_max_value(sample_list)
    print("Maximum Value:", max_val)