import collections
def sum_of_unique_numbers(data):
    unique_numbers = set(data)
    return sum(unique_numbers)
if __name__ == '__main__':
    sample_list = [1, 2, 2, 3, 4, 1, 5, 3]
    result = sum_of_unique_numbers(sample_list)
    print(result)