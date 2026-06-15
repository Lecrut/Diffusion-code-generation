import collections
def sum_of_unique_numbers(data):
    unique_numbers = set(data)
    return sum(unique_numbers)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 2, 1, 4, 3, 5]
    result = sum_of_unique_numbers(sample_list)
    print(result)