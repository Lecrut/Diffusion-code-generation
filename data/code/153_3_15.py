if __name__ == '__main__':
    sample_list = [1, 5, 2, 5, 8, 5, 3]
    target_value = 5
    result = any(x == target_value for x in sample_list)
    print(result)