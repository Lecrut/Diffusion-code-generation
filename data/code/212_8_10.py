def find_second_extremes(nums):
    if len(nums) < 2:
        return (None, None)
    first_min = second_min = float('inf')
    first_max = second_max = float('-inf')
    for num in nums:
        if num < first_min:
            second_min = first_min
            first_min = num
        elif first_min < num < second_min:
            second_min = num
        if num > first_max:
            second_max = first_max
            first_max = num
        elif first_max > num > second_max:
            second_max = num
    return (second_min if second_min != float('inf') else None, second_max if second_max != float('-inf') else None)
if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5, 1]
    print(find_second_extremes(sample_values))