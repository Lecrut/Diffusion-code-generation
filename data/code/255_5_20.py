import random

class MaxFinder:
    MAX_SIZE = 10

    @staticmethod
    def generate_random_list(size):
        return [random.randint(1, 100) for _ in range(size)]

    @staticmethod
    def find_max_value(lst):
        if not lst:
            return None
        max_val = lst[0]
        for value in lst[1:]:
            if value > max_val:
                max_val = value
        return max_val

if __name__ == '__main__':
    random_list = MaxFinder.generate_random_list(MaxFinder.MAX_SIZE)
    print("Random List:", random_list)
    max_value = MaxFinder.find_max_value(random_list)
    print("Max Value:", max_value)