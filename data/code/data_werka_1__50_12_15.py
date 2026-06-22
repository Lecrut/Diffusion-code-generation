class IntervalSet:
    def __init__(self, intervals):
        self.intervals = sorted(intervals)

    def merge_intervals(self):
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

    def find_difference(self, other_set):
        intervals2 = other_set.merge_intervals()
        i, j = 0, 0
        result = []
        while i < len(self.intervals) and j < len(intervals2):
            start1, end1 = self.intervals[i]
            start2, end2 = intervals2[j]
            if start1 > end2:
                j += 1
            elif start2 > end1:
                result.append((start1, end1))
                i += 1
            else:
                new_start = min(start1, start2)
                new_end = max(end1, end2)
                if start1 == start2 and end1 == end2:
                    i += 1
                    j += 1
                elif start1 <= start2 and end1 >= end2:
                    j += 1
                elif start1 >= start2 and end1 <= end2:
                    result.append((start1, new_end))
                    result.append((new_start, end1))
                    i += 1
                    j += 1
                else:
                    if start1 < start2:
                        result.append((start1, start2))
                    if end1 > end2:
                        result.append((end2, end1))
        while i < len(self.intervals):
            result.append(self.intervals[i])
            i += 1
        return IntervalSet(result).merge_intervals()

    def calculate_area(self):
        total_area = 0
        for start, end in self.merge_intervals():
            total_area += end - start
        return total_area

if __name__ == '__main__':
    set1 = IntervalSet([(1, 5), (8, 10)])
    set2 = IntervalSet([(3, 7), (6, 9)])

    difference_set = IntervalSet(set1.find_difference(set2))
    symmetric_difference_area = difference_set.calculate_area()

    print(symmetric_difference_area)