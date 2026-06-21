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

    symmetric_diff = set1.symmetric_difference(set2)
    result_intervals = []

    current_start = None
    for num in sorted(symmetric_diff):
        if current_start is None:
            current_start = num
        elif num != current_start + 1:
            result_intervals.append((current_start, num - 1))
            current_start = num

    if current_start is not None:
        result_intervals.append((current_start, max(symmetric_diff)))

    return merge_intervals(result_intervals)

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]
    print(symmetric_difference(intervals1, intervals2))