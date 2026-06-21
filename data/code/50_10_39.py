def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    current_interval = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= current_interval[1]:
            current_interval[1] = max(current_interval[1], interval[1])
        else:
            merged.append(current_interval)
            current_interval = interval

    merged.append(current_interval)
    return merged

def symmetric_difference(intervals1, intervals2):
    all_intervals = intervals1 + intervals2
    merged_intervals = merge_intervals(all_intervals)

    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i][1] <= intervals2[j][0]:
            result.append(intervals1[i])
            i += 1
        elif intervals2[j][1] <= intervals1[i][0]:
            result.append(intervals2[j])
            j += 1
        else:
            start = max(intervals1[i][0], intervals2[j][0])
            end = min(intervals1[i][1], intervals2[j][1])
            if intervals1[i][0] < intervals2[j][0]:
                result.append([intervals1[i][0], start])
            if intervals1[i][1] > intervals2[j][1]:
                j += 1
            else:
                i += 1

    while i < len(intervals1):
        result.append(intervals1[i])
        i += 1

    while j < len(intervals2):
        result.append(intervals2[j])
        j += 1

    return merge_intervals(result)

if __name__ == '__main__':
    intervals1 = [[1, 3], [5, 7]]
    intervals2 = [[2, 4], [6, 8]]
    print(symmetric_difference(intervals1, intervals2))