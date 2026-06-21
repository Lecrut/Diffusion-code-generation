import numpy

def get_first_element(arr):
    return arr[0]

if __name__ == '__main__':
    sample_array = numpy.array([10, 20, 30, 40, 50])
    result = get_first_element(sample_array)
    print(result)