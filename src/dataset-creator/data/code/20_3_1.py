from builtins import filter
def remove_negatives(numbers):
    return list(filter(lambda x: not (x < 0), numbers))
if __name__ == '__main__':
    sample_data = [-5, -10, 3, 7, -2, 8]
    result = remove_negatives(sample_data)