def extend_array(arr, times):
    arr[:] = arr * times

if __name__ == '__main__':
    sample_array = [1, 2, 3]
    extend_array(sample_array, 5)
    print(sample_array)