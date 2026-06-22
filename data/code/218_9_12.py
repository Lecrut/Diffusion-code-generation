import numpy as np

class MinFinder:
    @staticmethod
    def find_minimum(data):
        if not data.size:
            raise ValueError("Input array cannot be empty")
        minimum = data[0]
        for element in data[1:]:
            if element < minimum:
                minimum = element
        return minimum

if __name__ == '__main__':
    sample_array_1 = np.array([3, 1, 4, 1, 5, 9, 2])
    sample_array_2 = np.array([-10, 5, 0, -20, 15])
    sample_array_3 = np.array([42])
    sample_array_4 = np.array([])

    print(f"Array: {sample_array_1}")
    try:
        min1 = MinFinder.find_minimum(sample_array_1)
        print(f"Minimum element in {sample_array_1}: {min1}")
    except ValueError as e:
        print(e)

    print(f"Array 2: {sample_array_2}")
    try:
        min2 = MinFinder.find_minimum(sample_array_2)
        print(f"Minimum element in {sample_array_2}: {min2}")
    except ValueError as e:
        print(e)

    print(f"Array 3: {sample_array_3}")
    try:
        min3 = MinFinder.find_minimum(sample_array_3)
        print(f"Minimum element in {sample_array_3}: {min3}")
    except ValueError as e:
        print(e)

    print(f"Empty Array: {sample_array_4}")
    try:
        min4 = MinFinder.find_minimum(sample_array_4)
        print(f"Minimum element in {sample_array_4}: {min4}")
    except ValueError as e:
        print(e)