def find_minimum(numbers):
    return min([n for n in numbers])

if __name__ == '__main__':
    sample_list = [34, 15, 88, 2, 67]
    result = find_minimum(sample_list)
    print(result)