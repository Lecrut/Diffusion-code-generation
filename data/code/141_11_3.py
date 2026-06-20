import numpy as np

def custom_and(a, b):
    return np.logical_and(a, b)

def custom_or(a, b):
    return np.logical_or(a, b)

def custom_not(a):
    return np.logical_not(a)

if __name__ == '__main__':
    a = np.array([True, False, True, False])
    b = np.array([False, False, True, True])
    
    try:
        print("Custom AND:")
        print(custom_and(a, b))
        
        print("\nCustom OR:")
        print(custom_or(a, b))
        
        print("\nCustom NOT:")
        print(custom_not(a))
    except Exception as e:
        print(f"An error occurred: {e}")