def merge_intervals(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

def symmetric_difference(intervals1, intervals2):
    def find_difference(intervals1, intervals2):
        result = []
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            start1, end1 = intervals1[i]
            start2, end2 = intervals2[j]
            if end1 <= start2:
                result.append((start1, end1))
                i += 1
            elif end2 <= start1:
                result.append((start2, end2))
                j += 1
            else:
                if start1 < start2:
                    result.append((start1, start2))
                if end1 > end2:
                    result.append((end2, end1))
        while i < len(intervals1):
            result.append(intervals1[i])
            i += 1
        while j < len(intervals2):
            result.append(intervals2[j])
            j += 1
        return result

    merged1 = merge_intervals(intervals1)
    merged2 = merge_intervals(intervals2)
    diff1 = find_difference(merged1, merged2)
    diff2 = find_difference(merged2, merged1)
    total_area = sum(end - start for start, end in diff1 + diff2)
    return total_area

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]
    result = symmetric_difference(intervals1, intervals2)
    print(result)