def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

def symmetric_difference(intervals1, intervals2):
    combined = merge_intervals(intervals1 + intervals2)
    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i][0] <= intervals2[j][0]:
            if intervals1[i][1] <= intervals2[j][0]:
                result.append(intervals1[i])
                i += 1
            elif intervals1[i][1] <= intervals2[j][1]:
                result.append([intervals1[i][0], min(intervals1[i][1], intervals2[j][0])])
                i += 1
            else:
                result.append([intervals1[i][0], intervals2[j][0]])
        else:
            if intervals2[j][1] <= intervals1[i][0]:
                result.append(intervals2[j])
                j += 1
            elif intervals2[j][1] <= intervals1[i][1]:
                result.append([intervals2[j][0], min(intervals2[j][1], intervals1[i][0])])
                j += 1
            else:
                result.append([intervals2[j][0], intervals1[i][0]])
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