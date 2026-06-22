class IntervalSet:
    def __init__(self, intervals):
        self.intervals = sorted(intervals)

    def merge(self):
        if not self.intervals:
            return []
        merged = [self.intervals[0]]
        for current in self.intervals[1:]:
            last_merged = merged[-1]
            if current[0] <= last_merged[1]:
                merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
            else:
                merged.append(current)
        return merged

    def difference(self, other):
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
        while i < len(self.intervals):
            result.append(self.intervals[i])
            i += 1
        return result

def symmetric_difference(intervals1, intervals2):
    set1 = IntervalSet(intervals1)
    set2 = IntervalSet(intervals2)
    merged1 = set1.merge()
    merged2 = set2.merge()
    diff1 = set1.difference(set2)
    diff2 = set2.difference(set1)
    return diff1 + diff2

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]
    result = symmetric_difference(intervals1, intervals2)
    print(result)