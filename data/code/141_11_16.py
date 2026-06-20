import numpy as np

class LogicGates:
    @staticmethod
    def custom_and(a, b):
        return np.logical_and(a, b)

    @staticmethod
    def custom_or(a, b):
        return np.logical_or(a, b)

    @staticmethod
    def custom_not(a):
        return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])

    print("Custom AND:")
    print(LogicGates.custom_and(a, b))

    print("\nCustom OR:")
    print(LogicGates.custom_or(a, b))

    print("\nCustom NOT:")
    print(LogicGates.custom_not(a))