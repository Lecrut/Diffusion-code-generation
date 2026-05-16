def subtract_from_list(numbers, integer):
    return [x - integer for x in numbers]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    sample_integer = 7
    result = subtract_from_list(sample_list, sample_integer)
    print(result)