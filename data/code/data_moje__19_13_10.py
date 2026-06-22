import numpy

def get_random_element(arr):
    return arr[numpy.random.randint(0, arr.size)]

if __name__ == '__main__':
    large_array = numpy.arange(1000000)
    result = get_random_element(large_array)
    print(result)