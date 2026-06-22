class IntervalSet:
    def __init__(self, intervals):
        self.intervals = self.merge_intervals(intervals)

    def merge_intervals(self, intervals):
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

    def interval_difference(self, other):
        result = []
        i, j = 0, 0
        while i < len(self.intervals) and j < len(other.intervals):
            start1, end1 = self.intervals[i]
            start2, end2 = other.intervals[j]
            if end1 <= start2:
                result.append((start1, end1))
                i += 1
            elif end2 <= start1:
                j += 1
            else:
                if start1 < start2:
                    result.append((start1, start2))
                if end1 > end2:
                    i += 1
                    self.intervals[i-1] = (end2, end1)
                else:
                    i += 1
                    j += 1
        result.extend(self.intervals[i:])
        return IntervalSet(result)

    def symmetric_difference(self, other):
        diff1 = self.interval_difference(other)
        diff2 = other.interval_difference(self)
        return diff1.merge_intervals(diff2.intervals + diff1.intervals)

def main():
    intervals1 = [(1, 3), (5, 7)]
    intervals2 = [(2, 4), (6, 8)]
    set1 = IntervalSet(intervals1)
    set2 = IntervalSet(intervals2)
    sym_diff = set1.symmetric_difference(set2)
    print(sym_diff.intervals)

if __name__ == '__main__':
    main()