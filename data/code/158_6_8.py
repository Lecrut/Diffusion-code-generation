import numpy as np

if __name__ == '__main__':
    array = np.arange(1, 21)
    even_numbers = array[array % 2 == 0]
    print(even_numbers)