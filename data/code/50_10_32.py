def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    current_start, current_end = intervals[0]
    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end
    merged.append((current_start, current_end))
    return merged

def symmetric_difference(intervals1, intervals2):
    def interval_to_set(interval):
        return set(range(interval[0], interval[1] + 1))
    
    set1 = set()
    for interval in intervals1:
        set1.update(interval_to_set(interval))

    set2 = set()
    for interval in intervals2:
        set2.update(interval_to_set(interval))

    symmetric_diff_set = set1.symmetric_difference(set2)

    def set_to_intervals(s):
        result = []
        current_start = None
        for num in sorted(s):
            if current_start is None:
                current_start = num
            elif num != current_start + 1:
                result.append((current_start, num - 1))
                current_start = num
        if current_start is not None:
            result.append((current_start, max(s)))
        return result

    return set_to_intervals(symmetric_diff_set)

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 11)]
    print(symmetric_difference(intervals1, intervals2))