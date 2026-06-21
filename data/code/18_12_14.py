def median_index(values):
    if not values:
        raise ValueError("List is empty")
    length = len(values)
    middle = length // 2
    if length % 2 == 0:
        low_idx = -1
        for i in range(length):
            count_smaller = 0
            count_equal = 0
            for j in range(length):
                if values[j] < values[i]:
                    count_smaller += 1
                elif values[j] == values[i]:
                    count_equal += 1
            rank_low = count_smaller + 1
            rank_high = count_smaller + count_equal
            if rank_low <= middle and rank_high >= middle:
                low_idx = i
                break
        high_idx = -1
        for i in range(length):
            count_smaller = 0
            count_equal = 0
            for j in range(length):
                if values[j] < values[i]:
                    count_smaller += 1
                elif values[j] == values[i]:
                    count_equal += 1
            rank_low = count_smaller + 1
            rank_high = count_smaller + count_equal
            if rank_low <= middle + 1 and rank_high >= middle + 1:
                high_idx = i
                break
        return (values[low_idx] + values[high_idx]) / 2
    else:
        for i in range(length):
            count_smaller = 0
            count_equal = 0
            for j in range(length):
                if values[j] < values[i]:
                    count_smaller += 1
                elif values[j] == values[i]:
                    count_equal += 1
            rank_low = count_smaller + 1
            rank_high = count_smaller + count_equal
            if rank_low <= middle + 1 and rank_high >= middle + 1:
                return values[i]

if __name__ == '__main__':
    sample1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sample2 = [1, 2, 3, 4]
    sample3 = [7]
    sample4 = [10, 20, 30, 40, 50, 60]

    result1 = median_index(sample1)
    result2 = median_index(sample2)
    result3 = median_index(sample3)
    result4 = median_index(sample4)

    print(result1)
    print(result2)
    print(result3)
    print(result4)