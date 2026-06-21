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

    def symmetric_difference(self, other):
        all_intervals = sorted(self.intervals + other.intervals)
        symmetric_diff = []
        i, j = 0, 0
        while i < len(self.intervals) and j < len(other.intervals):
            start1, end1 = self.intervals[i]
            start2, end2 = other.intervals[j]
            if end1 < start2:
                symmetric_diff.append((start1, end1))
                i += 1
            elif end2 < start1:
                symmetric_diff.append((start2, end2))
                j += 1
            else:
                low = min(start1, start2)
                high = max(end1, end2)
                if start1 <= start2 and end1 >= end2:
                    i += 1
                elif start2 <= start1 and end2 >= end1:
                    j += 1
                elif start1 < start2:
                    symmetric_diff.append((start1, start2))
                    i += 1
                elif start2 < start1:
                    symmetric_diff.append((start2, start1))
                    j += 1
        while i < len(self.intervals):
            symmetric_diff.append(self.intervals[i])
            i += 1
        while j < len(other.intervals):
            symmetric_diff.append(other.intervals[j])
            j += 1
        return IntervalSet(symmetric_diff)

    def __repr__(self):
        return str(self.intervals)

if __name__ == '__main__':
    intervals1 = [(1, 3), (5, 7)]
    intervals2 = [(2, 4), (6, 8)]
    set1 = IntervalSet(intervals1)
    set2 = IntervalSet(intervals2)
    result_set = set1.symmetric_difference(set2)
    print(result_set)