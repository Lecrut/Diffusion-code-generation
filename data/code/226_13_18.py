def extend_array(arr, times):
    arr[:] = (arr * times)[:len(arr)]

if __name__ == '__main__':
    sample_arr = [1, 2, 3]
    extend_array(sample_arr, 5)
    print(sample_arr)