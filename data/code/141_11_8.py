import numpy as np

class LogicGates:
    def custom_and(self, a, b):
        return np.logical_and(a, b)
    
    def custom_or(self, a, b):
        return np.logical_or(a, b)
    
    def custom_not(self, a):
        return np.logical_not(a)

if __name__ == '__main__':
    logic = LogicGates()
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    print("Custom AND:")
    print(logic.custom_and(a, b))
    print("\nCustom OR:")
    print(logic.custom_or(a, b))
    print("\nCustom NOT (a):")
    print(logic.custom_not(a))
    print("\nCustom NOT (b):")
    print(logic.custom_not(b))