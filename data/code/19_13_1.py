import numpy

def get_random_element(arr):
    index = numpy.random.randint(0, arr.size)
    return arr.flat[index]

if __name__ == '__main__':
    sample_array = numpy.arange(1000)
    result = get_random_element(sample_array)
    print(result)