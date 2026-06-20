import numpy as np

class ArithmeticOperations:
    def __init__(self, list1, list2):
        self.array1 = np.array(list1)
        self.array2 = np.array(list2)

    def perform_operations(self):
        addition_result = self.array1 + self.array2
        subtraction_result = self.array1 - self.array2
        multiplication_result = self.array1 * self.array2
        division_result = self.array1 / self.array2
        return addition_result, subtraction_result, multiplication_result, division_result

if __name__ == '__main__':
    sample_list1 = [10, 20]
    sample_list2 = [5, 3]
    operations = ArithmeticOperations(sample_list1, sample_list2)
    results = operations.perform_operations()
    print("Addition:", results[0])
    print("Subtraction:", results[1])
    print("Multiplication:", results[2])
    print("Division:", results[3])