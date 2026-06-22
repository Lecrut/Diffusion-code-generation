import numpy as np

def repeat_array(array, repetitions):
    result = np.repeat(array, repetitions, axis=0)
    return result

if __name__ == '__main__':
    sample_array = [1.1, 2.2, 3.3]
    repeats = 3
    repeated_result = repeat_array(sample_array, repeats)
    print(repeated_result)