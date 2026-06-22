class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def merge(intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        merged = [intervals[0]]
        for current in intervals[1:]:
            last_merged = merged[-1]
            if current.start <= last_merged.end:
                merged[-1] = Interval(last_merged.start, max(last_merged.end, current.end))
            else:
                merged.append(current)
        return merged

    @staticmethod
    def interval_to_set(interval):
        return set(range(interval.start, interval.end + 1))

def symmetric_difference(intervals1, intervals2):
    def to_interval_objects(intervals):
        return [Interval(start, end) for start, end in intervals]

    intervals1 = to_interval_objects(intervals1)
    intervals2 = to_interval_objects(intervals2)

    merged1 = Interval.merge(intervals1)
    merged2 = Interval.merge(intervals2)

    set1 = set()
    set2 = set()

    for interval in merged1:
        set1.update(Interval.interval_to_set(interval))

    for interval in merged2:
        set2.update(Interval.interval_to_set(interval))

    symmetric_diff = (set1 - set2).union(set2 - set1)
    return sorted(list(symmetric_diff))

if __name__ == '__main__':
    intervals1 = [(1, 3), (5, 7)]
    intervals2 = [(2, 4), (6, 8)]
    result = symmetric_difference(intervals1, intervals2)
    print(result)