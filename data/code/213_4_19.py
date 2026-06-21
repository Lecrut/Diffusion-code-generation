SORT_KEY = lambda x: -x

def sort_descending(numbers):
    numbers.sort(key=SORT_KEY)
    return numbers
if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 0.7]
    sorted_values = sort_descending(sample_values)
    print(sorted_values)