def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)

    return merged

def symmetric_difference(intervals1, intervals2):
    combined = merge_intervals(intervals1 + intervals2)
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
            if intervals1[i][0] < intervals2[j][0]:
                result.append((intervals1[i][0], min(intervals1[i][1], intervals2[j][0])))
            if intervals1[i][1] > intervals2[j][1]:
                result.append((max(intervals1[i][0], intervals2[j][1]), intervals1[i][1]))
            i += 1
            j += 1

    while i < len(intervals1):
        result.append(intervals1[i])
        i += 1

    while j < len(intervals2):
        result.append(intervals2[j])
        j += 1

    return merge_intervals(result)

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]
    print(symmetric_difference(intervals1, intervals2))