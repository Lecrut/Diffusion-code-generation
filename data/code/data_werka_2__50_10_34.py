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
    def interval_to_set(interval):
        return set(range(interval[0], interval[1] + 1))
    
    def union_sets(set1, set2):
        return set1.union(set2)
    
    def difference_sets(set1, set2):
        return set1.difference(set2)
    
    if not all(isinstance(i, tuple) and len(i) == 2 and i[0] <= i[1] for i in intervals1 + intervals2):
        raise ValueError("All intervals must be tuples of two integers where the first integer is less than or equal to the second.")
    
    set1 = union_sets(*[interval_to_set(interval) for interval in intervals1])
    set2 = union_sets(*[interval_to_set(interval) for interval in intervals2])
    
    diff1 = difference_sets(set1, set2)
    diff2 = difference_sets(set2, set1)
    
    combined_diff = diff1.union(diff2)
    
    def set_to_intervals(s):
        result = []
        current_start = None
        for number in sorted(combined_diff):
            if current_start is None:
                current_start = number
            elif number != current_start + 1:
                result.append((current_start, number - 1))
                current_start = number
        if current_start is not None:
            result.append((current_start, max(combined_diff)))
        return result
    
    return merge_intervals(set_to_intervals(combined_diff))

if __name__ == '__main__':
    intervals1 = [(1, 3), (5, 7)]
    intervals2 = [(2, 4), (6, 8)]
    print(symmetric_difference(intervals1, intervals2))