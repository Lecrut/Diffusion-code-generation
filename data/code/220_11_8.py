import numpy as np

class SetAverageCalculator:
    @staticmethod
    def calculate_averages(list_of_lists):
        averages = []
        for inner_list in list_of_lists:
            if inner_list:
                average = np.mean(inner_list)
                averages.append(average)
            else:
                averages.append(0)
        return averages

if __name__ == '__main__':
    sample_data = [
        [1, 2, 3],
        [10, 20],
        [5, 5, 5, 5]
    ]
    calculator = SetAverageCalculator()
    result = calculator.calculate_averages(sample_data)
    print(result)