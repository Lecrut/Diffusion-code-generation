def symmetric_difference(intervals1, intervals2):

    def merge_intervals(intervals):
        intervals.sort()
        merged = []
        for start, end in intervals:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

    def interval_area(interval):
        return interval[1] - interval[0]

    def calculate_difference(intervals1, intervals2):
        result = []
        i, j = (0, 0)
        while i < len(intervals1) and j < len(intervals2):
            start1, end1 = intervals1[i]
            start2, end2 = intervals2[j]
            if end1 <= start2:
                result.append([start1, end1])
                i += 1
            elif end2 <= start1:
                result.append([start2, end2])
                j += 1
            else:
                if start1 < start2:
                    result.append([start1, start2])
                if end1 > end2:
                    result.append([end2, end1])
                i += 1
                j += 1
        while i < len(intervals1):
            result.append(intervals1[i])
            i += 1
        while j < len(intervals2):
            result.append(intervals2[j])
            j += 1
        return result
    merged1 = merge_intervals(intervals1)
    merged2 = merge_intervals(intervals2)
    diff_intervals = calculate_difference(merged1, merged2)
    total_area = sum((interval_area(interval) for interval in diff_intervals))
    return total_area
if __name__ == '__main__':
    intervals1 = [(1, 5), (7, 10)]
    intervals2 = [(3, 6), (8, 12)]
    print(symmetric_difference(intervals1, intervals2))