def check_equality(item1, item2):
    return item1 is item2 and item1 == item2
if __name__ == '__main__':
    sample_value1 = [1, 2, 3]
    sample_value2 = sample_value1
    sample_value3 = [1, 2, 3]
    print(check_equality(sample_value1, sample_value2))
    print(check_equality(sample_value1, sample_value3))