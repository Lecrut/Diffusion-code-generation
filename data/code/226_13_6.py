def extend_array(arr, times):
    arr.extend(arr * (times - 1))

if __name__ == '__main__':
    sample = [1, 2, 3]
    extend_array(sample, 5)
    print(sample)