import numpy

def get_first_element(arr):
    return arr.flat[0]

if __name__ == '__main__':
    data = numpy.array([[10, 20], [30, 40]])
    result = get_first_element(data)
    print(result)