class IntervalSet:
    def __init__(self, intervals):
        self.intervals = intervals

    def merge_intervals(self):
        if not self.intervals:
            return []
        self.intervals.sort()
        merged = [self.intervals[0]]
        for current in self.intervals[1:]:
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:
                merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
            else:
                merged.append(current)
        return merged

    def symmetric_difference(self, other):
        combined = self.merge_intervals() + other.merge_intervals()
        combined.sort()
        result = []
        i, j = 0, 0
        while i < len(combined) and j < len(other.intervals):
            start1, end1 = combined[i]
            start2, end2 = other.intervals[j]
            if end1 <= start2:
                result.append((start1, end1))
                i += 1
            elif end2 <= start1:
                result.append((start2, end2))
                j += 1
            else:
                if start1 < start2:
                    result.append((start1, start2))
                if end1 > end2:
                    result.append((end2, end1))
        result.extend(combined[i:])
        result.extend(other.intervals[j:])
        return IntervalSet(result)

    def calculate_area(self):
        area = 0
        for start, end in self.intervals:
            area += end - start
        return area

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]

    set1 = IntervalSet(intervals1)
    set2 = IntervalSet(intervals2)

    sym_diff = set1.symmetric_difference(set2)
    print("Symmetric Difference Intervals:", sym_diff.intervals)
    print("Area of Symmetric Difference:", sym_diff.calculate_area())