def symmetric_difference(intervals1, intervals2):
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

    def interval_difference(intervals1, intervals2):
        result = []
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            start1, end1 = intervals1[i]
            start2, end2 = intervals2[j]
            if end1 <= start2:
                result.append((start1, end1))
                i += 1
            elif end2 <= start1:
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
        return result

    merged1 = merge_intervals(intervals1)
    merged2 = merge_intervals(intervals2)

    diff1 = interval_difference(merged1, merged2)
    diff2 = interval_difference(merged2, merged1)

    return merge_intervals(diff1 + diff2)

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10), (15, 20)]
    intervals2 = [(3, 7), (9, 11), (16, 18)]

    result = symmetric_difference(intervals1, intervals2)
    print(result)