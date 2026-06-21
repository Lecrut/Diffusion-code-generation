import numpy as np

class SampleValues:
    VALUES = [100, 200, 300]

    @staticmethod
    def calculate_average():
        return np.mean(SampleValues.VALUES)

if __name__ == '__main__':
    average = SampleValues.calculate_average()
    print(average)