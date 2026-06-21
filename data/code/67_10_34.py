def find_pair_with_sum(arr, target):
    LEFT_INDEX = 0
    RIGHT_INDEX = len(arr) - 1
    
    while LEFT_INDEX < RIGHT_INDEX:
        current_sum = arr[LEFT_INDEX] + arr[RIGHT_INDEX]
        if current_sum == target:
            return (arr[LEFT_INDEX], arr[RIGHT_INDEX])
        elif current_sum < target:
            LEFT_INDEX += 1
        else:
            RIGHT_INDEX -= 1
    raise ValueError("No two elements sum up to the target value")

if __name__ == '__main__':
    sample_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_value = 17
    result = find_pair_with_sum(sample_array, target_value)
    print(result)