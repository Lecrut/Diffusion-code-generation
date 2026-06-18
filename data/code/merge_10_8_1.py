import collections
def sum_unique_numbers(data):
    unique_numbers = set(data)
    return sum(unique_numbers)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 1, 4, 5, 3]
    result = sum_unique_numbers(sample_list)
    print(result)