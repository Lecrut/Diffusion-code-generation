class Interval:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start of interval cannot be greater than end")
        self.start = start
        self.end = end

    def length(self):
        return self.end - self.start

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x.start)
    merged = []
    for interval in intervals:
        if not merged or merged[-1].end < interval.start:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)
    return merged

def symmetric_difference(intervals1, intervals2):
    all_intervals = intervals1 + intervals2
    for interval in all_intervals:
        if not isinstance(interval, Interval):
            raise ValueError("All elements must be instances of Interval")
    combined = merge_intervals(all_intervals)
    result = []
    i, j = 0, 0
    while i < len(intervals1) and j < len(intervals2):
        start1, end1 = intervals1[i].start, intervals1[i].end
        start2, end2 = intervals2[j].start, intervals2[j].end
        if end1 <= start2:
            result.append(Interval(start1, end1))
            i += 1
        elif end2 <= start1:
            result.append(Interval(start2, end2))
            j += 1
        else:
            if start1 < start2:
                result.append(Interval(start1, start2))
            if end1 > end2:
                result.append(Interval(end2, end1))
            i += 1
            j += 1
    while i < len(intervals1):
        result.append(intervals1[i])
        i += 1
    while j < len(intervals2):
        result.append(intervals2[j])
        j += 1
    return sum(interval.length() for interval in merge_intervals(result))

if __name__ == '__main__':
    intervals1 = [Interval(1, 5), Interval(8, 10)]
    intervals2 = [Interval(3, 7), Interval(9, 12)]
    print(symmetric_difference(intervals1, intervals2))