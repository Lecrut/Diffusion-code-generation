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

    def interval_difference(interval1, interval2):
        start1, end1 = interval1
        start2, end2 = interval2
        
        if end1 <= start2 or end2 <= start1:
            return [interval1]
        
        result = []
        if start1 < start2:
            result.append((start1, start2))
        if end1 > end2:
            result.append((end2, end1))
        
        return result

    all_intervals = intervals1 + intervals2
    merged_intervals = merge_intervals(all_intervals)
    
    symmetric_diff = []
    for i in range(len(merged_intervals) - 1):
        diff = interval_difference(merged_intervals[i], merged_intervals[i + 1])
        symmetric_diff.extend(diff)
    
    return symmetric_diff

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]
    result = symmetric_difference(intervals1, intervals2)
    print(result)