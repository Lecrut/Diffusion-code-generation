def cumulative_sum(arr):
    result = []
    current_sum = 0
    for num in arr:
        current_sum += num
        result.append(current_sum)
    return result

if __name__ == '__main__':
    sample_array = [1, 2, 3, 4, 5]
    print(cumulative_sum(sample_array))