import numpy

def calculate_mean(data):
    return numpy.mean(data)

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    result = calculate_mean(test_data)
    print(result)