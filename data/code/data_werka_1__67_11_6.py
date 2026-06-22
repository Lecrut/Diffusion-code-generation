def find_pair_with_sum(arr, target):
    LEFT = 0
    RIGHT = len(arr) - 1
    
    while LEFT < RIGHT:
        current_sum = arr[LEFT] + arr[RIGHT]
        if current_sum == target:
            return (arr[LEFT], arr[RIGHT])
        elif current_sum < target:
            LEFT += 1
        else:
            RIGHT -= 1
    return None

if __name__ == '__main__':
    sample_array = [1, 3, 5, 7, 9, 11]
    target_value = 10
    result = find_pair_with_sum(sample_array, target_value)
    print(result)