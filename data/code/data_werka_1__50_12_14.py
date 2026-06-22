class Interval:
    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start of interval must be less than or equal to end.")
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
    def find_difference(intervals1, intervals2):
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
                left = min(intervals1[i].start, intervals2[j].start)
                right = max(intervals1[i].end, intervals2[j].end)
                if intervals1[i].start < intervals2[j].start:
                    result.append(Interval(left, intervals2[j].start))
                elif intervals2[j].start < intervals1[i].start:
                    result.append(Interval(left, intervals1[i].start))
                i += 1
                j += 1
        while i < len(intervals1):
            result.append(intervals1[i])
            i += 1
        while j < len(intervals2):
            result.append(intervals2[j])
            j += 1
        return merge_intervals(result)

    merged1 = merge_intervals(intervals1)
    merged2 = merge_intervals(intervals2)
    diff1 = find_difference(merged1, merged2)
    diff2 = find_difference(merged2, merged1)
    return diff1 + diff2

def calculate_area(intervals):
    return sum(interval.end - interval.start for interval in intervals)

if __name__ == '__main__':
    try:
        intervals1 = [Interval(1, 5), Interval(8, 10)]
        intervals2 = [Interval(3, 7), Interval(9, 12)]
        sym_diff_intervals = symmetric_difference(intervals1, intervals2)
        area = calculate_area(sym_diff_intervals)
        print(area)
    except Exception as e:
        print(e)