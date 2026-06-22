import random

class RandomMaxFinder:
    MAX_RANDOM_VALUE = 1000
    
    @staticmethod
    def generate_random_list(size):
        return [random.randint(0, RandomMaxFinder.MAX_RANDOM_VALUE) for _ in range(size)]
    
    @staticmethod
    def find_max_value(data):
        if not data:
            raise ValueError("Data cannot be empty")
        max_value = data[0]
        for element in data[1:]:
            if element > max_value:
                max_value = element
        return max_value

if __name__ == '__main__':
    random_list = RandomMaxFinder.generate_random_list(10)
    print("Random List:", random_list)
    max_value = RandomMaxFinder.find_max_value(random_list)
    print("Maximum Value:", max_value)