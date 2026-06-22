class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return max(0, self.end - self.start)

class IntervalSet:
    @staticmethod
    def merge_intervals(intervals):
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
    def find_difference(intervals1, intervals2):
        result = []
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            start1, end1 = intervals1[i].start, intervals1[i].end
            start2, end2 = intervals2[j].start, intervals2[j].end

            if start1 > end2:
                result.append(Interval(start1, end1))
                j += 1
            elif start2 > end1:
                i += 1
            else:
                if start1 < start2:
                    result.append(Interval(start1, start2))
                if end1 > end2:
                    i += 1
                else:
                    j += 1

        while i < len(intervals1):
            result.append(intervals1[i])
            i += 1

        return result

    @staticmethod
    def symmetric_difference_area(intervals1, intervals2):
        merged1 = IntervalSet.merge_intervals(intervals1)
        merged2 = IntervalSet.merge_intervals(intervals2)
        diff1 = IntervalSet.find_difference(merged1, merged2)
        diff2 = IntervalSet.find_difference(merged2, merged1)
        total_area = sum(interval.length() for interval in diff1) + sum(interval.length() for interval in diff2)
        return total_area

if __name__ == '__main__':
    intervals1 = [Interval(1, 5), Interval(8, 10)]
    intervals2 = [Interval(3, 7), Interval(9, 12)]
    print(IntervalSet.symmetric_difference_area(intervals1, intervals2))