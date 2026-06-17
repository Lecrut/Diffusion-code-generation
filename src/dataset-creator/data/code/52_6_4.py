def final_value_explicit(nums):
    result = 0
    for n in nums:
        if n % 2 == 1:
            result += 1
        else:
            result -= 1
    return result
if __name__ == '__main__':
    sample_list = [3, -7, 5, 4, -9]
    print(final_value_explicit(sample_list))