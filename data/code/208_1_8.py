import numpy as np

class ArrayStats:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0
        return np.mean(np.array(numbers))

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10.5, 20.5, 30.5]
    empty_list = []
    list3 = [-1, 5, 10, -2]

    stats_calculator = ArrayStats()
    mean1 = stats_calculator.calculate_mean(list1)
    mean2 = stats_calculator.calculate_mean(list2)
    mean_empty = stats_calculator.calculate_mean(empty_list)
    mean3 = stats_calculator.calculate_mean(list3)

    print(f"Mean of {list1}: {mean1}")
    print(f"Mean of {list2}: {mean2}")
    print(f"Mean of {empty_list}: {mean_empty}")
    print(f"Mean of {list3}: {mean3}")