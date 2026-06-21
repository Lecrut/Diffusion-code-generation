import numpy as np

def filter_even_numbers():
    array = np.arange(1, 21)
    even_numbers = array[array % 2 == 0]
    return even_numbers

if __name__ == '__main__':
    result = filter_even_numbers()
    print(result)