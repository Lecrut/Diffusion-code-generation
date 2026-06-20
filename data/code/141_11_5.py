import numpy as np

class CustomLogicGates:
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
    print(CustomLogicGates.custom_and(a, b))
    
    print("\nCustom OR:")
    print(CustomLogicGates.custom_or(a, b))
    
    print("\nCustom NOT:")
    print(CustomLogicGates.custom_not(a))