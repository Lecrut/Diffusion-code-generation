if __name__ == '__main__':
    sample_list = [3, 5, 8, 10]
    target_value = 9
    result = any(x > target_value for x in sample_list)
    print(result)