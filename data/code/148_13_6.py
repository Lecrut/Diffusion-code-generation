def find_max_element(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    return max(numbers)

if __name__ == '__main__':
    sample_list = [3.5, 1.2, 7.8, 4.4]
    print(find_max_element(sample_list))