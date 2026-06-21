if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    if not all(isinstance(item, int) for item in sample_list):
        raise ValueError("All elements in the list must be integers")
    total_sum = sum(x for x in sample_list)
    print(total_sum)