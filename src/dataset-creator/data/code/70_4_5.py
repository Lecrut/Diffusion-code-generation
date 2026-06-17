def compare_distances(distance_pairs, target1, target2):
    results = []
    for dist in distance_pairs:
        if abs(dist[0] - target1) < 0.5 and abs(dist[1] - target2) < 0.5:
            results.append(True)
        else:
            results.append(False)
    return results
if __name__ == '__main__':
    distances = [(3.4, 7.8), (6.9, 2.1), (10.0, 10.5)]
    t1, t2 = 3.5, 7.9
    matches = compare_distances(distances, t1, t2)
    print(matches)