def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if merged and merged[-1][1] >= interval[0]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(interval)
    return merged

def symmetric_difference(intervals1, intervals2):
    def interval_to_points(intervals):
        points = set()
        for start, end in intervals:
            points.add((start, 'S'))
            points.add((end + 1, 'E'))
        return points

    points1 = interval_to_points(intervals1)
    points2 = interval_to_points(intervals2)

    all_points = sorted(points1.union(points2))
    balance = 0
    result = []
    current_start = None

    for point, event in all_points:
        if balance == 1 and current_start is None:
            current_start = point
        elif balance == 0 and current_start is not None:
            result.append((current_start, point - 1))
            current_start = None

        if event == 'S':
            balance += 1
        else:
            balance -= 1

    return merge_intervals(result)

if __name__ == '__main__':
    intervals1 = [(1, 3), (5, 7)]
    intervals2 = [(2, 4), (6, 8)]
    print(symmetric_difference(intervals1, intervals2))