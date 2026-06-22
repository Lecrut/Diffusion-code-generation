import numpy as np

def get_random_element(arr):
    if not arr.size:
        raise ValueError("Cannot choose from empty array")
    return np.random.choice(arr.ravel())

if __name__ == '__main__':
    test_data = np.linspace(0, 100, 500000)
    selected = get_random_element(test_data)
    print(selected)