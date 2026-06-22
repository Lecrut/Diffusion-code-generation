def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    return merged

def interval_difference(intervals1, intervals2):
    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i]
        start2, end2 = intervals2[j]
        
        if end1 < start2:
            result.append((start1, end1))
            i += 1
        elif end2 < start1:
            result.append((start2, end2))
            j += 1
        else:
            if start1 < start2:
                result.append((start1, start2))
            if end1 > end2:
                intervals1[i] = (end2, end1)
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

def symmetric_difference(intervals1, intervals2):
    if not all(isinstance(i, tuple) and len(i) == 2 and i[0] <= i[1] for i in intervals1 + intervals2):
        raise ValueError("All intervals must be tuples of two integers where the first integer is less than or equal to the second.")
    
    diff1 = interval_difference(intervals1, intervals2)
    diff2 = interval_difference(intervals2, intervals1)
    return merge_intervals(diff1 + diff2)

if __name__ == '__main__':
    intervals1 = [(1, 3), (5, 7)]
    intervals2 = [(2, 4), (6, 8)]
    print(symmetric_difference(intervals1, intervals2))