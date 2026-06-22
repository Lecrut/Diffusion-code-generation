def find_the_middle_value_among_three_convert_all(nums):
    return sorted(nums)[1]

if __name__ == '__main__':
    sample_values = [10, 5, 15]
    middle = find_the_middle_value_among_three_convert_all(sample_values)
    print(middle)