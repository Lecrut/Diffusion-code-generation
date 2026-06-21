MAX_LIST_LENGTH = 1000

def find_max_element(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_list = [34, 56, 78, 90, 23]
    largest = find_max_element(sample_list)
    print(largest)