def sum_three(data):
    a, b, c = data
    return a + b + c
if __name__ == '__main__':
    sample_tuple = (10, 20, 30)
    result = sum_three(sample_tuple)
    print(result)