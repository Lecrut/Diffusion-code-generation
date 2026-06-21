def find_largest(numbers):
    if not numbers:
        return None
    return max(numbers)
if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_largest(sample_list))
    empty_list = []
    print(find_largest(empty_list))