def compare_distances(distance_pairs, target1, target2):
    results = []
    for dist in distance_pairs:
        if abs(dist[0] - target1) < 0.5 and abs(dist[1] - target2) < 0.5:
            results.append(True)
        else:
            results.append(False)
    return results
if __name__ == '__main__':
    distance_data = [(3.4, 7.8), (6.1, 9.2), (2.9, 8.0)]
    target_a = 5.0
    target_b = 8.0
    matches = compare_distances(distance_data, target_a, target_b)
    for i, match in enumerate(matches):
        print(f"Pair {i+1}: {'Match' if match else 'No Match'}")