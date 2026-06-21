def find_odd_numbers(nums):
    return [num for num in nums if num & 1]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_odd_numbers(sample_values))