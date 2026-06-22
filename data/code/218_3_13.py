if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    if not sample_list:
        raise ValueError("Input list cannot be empty")
    minimum_value = min(sample_list)
    print(minimum_value)