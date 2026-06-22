def symmetric_difference(intervals1, intervals2):
    def merge_intervals(intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        current_start, current_end = intervals[0]

        for start, end in intervals[1:]:
            if start <= current_end:
                current_end = max(current_end, end)
            else:
                merged.append((current_start, current_end))
                current_start, current_end = start, end

        merged.append((current_start, current_end))
        return merged

    def find_symmetric_difference(intervals1, intervals2):
        all_intervals = sorted(intervals1 + intervals2)
        symmetric_diff = []
        i, j = 0, 0
        while i < len(intervals1) and j < len(intervals2):
            if intervals1[i][1] <= intervals2[j][0]:
                symmetric_diff.append(intervals1[i])
                i += 1
            elif intervals2[j][1] <= intervals1[i][0]:
                symmetric_diff.append(intervals2[j])
                j += 1
            else:
                if intervals1[i][0] < intervals2[j][0]:
                    symmetric_diff.append((intervals1[i][0], intervals2[j][0]))
                if intervals1[i][1] > intervals2[j][1]:
                    symmetric_diff.append((intervals2[j][1], intervals1[i][1]))
                i += 1
                j += 1

        while i < len(intervals1):
            symmetric_diff.append(intervals1[i])
            i += 1

        while j < len(intervals2):
            symmetric_diff.append(intervals2[j])
            j += 1

        return merge_intervals(symmetric_diff)

    intervals1 = merge_intervals(intervals1)
    intervals2 = merge_intervals(intervals2)
    return find_symmetric_difference(intervals1, intervals2)

if __name__ == '__main__':
    intervals1 = [(1, 5), (8, 10)]
    intervals2 = [(3, 7), (9, 12)]
    result = symmetric_difference(intervals1, intervals2)
    print(result)