class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x.start)
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current.start <= last_merged.end:
            merged[-1] = Interval(last_merged.start, max(last_merged.end, current.end))
        else:
            merged.append(current)
    return merged

def find_symmetric_difference(intervals1, intervals2):
    combined = merge_intervals(intervals1 + intervals2)
    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i].end <= intervals2[j].start:
            result.append(intervals1[i])
            i += 1
        elif intervals2[j].end <= intervals1[i].start:
            result.append(intervals2[j])
            j += 1
        else:
            if intervals1[i].start < intervals2[j].start:
                result.append(Interval(intervals1[i].start, intervals2[j].start))
            if intervals1[i].end > intervals2[j].end:
                result.append(Interval(intervals2[j].end, intervals1[i].end))
            i += 1
            j += 1
    while i < len(intervals1):
        result.append(intervals1[i])
        i += 1
    while j < len(intervals2):
        result.append(intervals2[j])
        j += 1
    return merge_intervals(result)

def calculate_area(intervals):
    return sum(interval.end - interval.start for interval in intervals)

if __name__ == '__main__':
    intervals1 = [Interval(1, 5), Interval(8, 10)]
    intervals2 = [Interval(3, 7), Interval(9, 12)]
    
    symmetric_diff_intervals = find_symmetric_difference(intervals1, intervals2)
    symmetric_diff_area = calculate_area(symmetric_diff_intervals)
    
    print(symmetric_diff_area)