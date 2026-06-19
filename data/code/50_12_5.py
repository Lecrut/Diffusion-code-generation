class Interval:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start of interval must be less than or equal to end")
        self.start = start
        self.end = end

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
    def find_difference(intervals_a, intervals_b):
        result = []
        i, j = 0, 0
        while i < len(intervals_a) and j < len(intervals_b):
            if intervals_a[i].end <= intervals_b[j].start:
                result.append(intervals_a[i])
                i += 1
            elif intervals_b[j].end <= intervals_a[i].start:
                result.append(intervals_b[j])
                j += 1
            else:
                left = min(intervals_a[i].start, intervals_b[j].start)
                right = max(intervals_a[i].end, intervals_b[j].end)
                if intervals_a[i].start < intervals_b[j].start:
                    result.append(Interval(intervals_a[i].start, intervals_b[j].start))
                    intervals_a[i].start = intervals_b[j].start
                elif intervals_b[j].start < intervals_a[i].start:
                    result.append(Interval(intervals_b[j].start, intervals_a[i].start))
                    intervals_b[j].start = intervals_a[i].start
                if intervals_a[i].end > intervals_b[j].end:
                    intervals_a[i].start = intervals_b[j].end
                else:
                    intervals_b[j].start = intervals_a[i].end
        result.extend(intervals_a[i:])
        result.extend(intervals_b[j:])
        return merge_intervals(result)

    merged1 = merge_intervals(intervals1)
    merged2 = merge_intervals(intervals2)
    return find_difference(merged1, merged2)

if __name__ == '__main__':
    intervals1 = [Interval(1, 5), Interval(8, 10)]
    intervals2 = [Interval(3, 7), Interval(9, 12)]
    result = symmetric_difference(intervals1, intervals2)
    for interval in result:
        print(f"({interval.start}, {interval.end})")