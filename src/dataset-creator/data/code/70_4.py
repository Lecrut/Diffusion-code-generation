distances = [(10, 20), (30, 40), (50, 60)]
targets_a = [15]
targets_b = [35]
results = []
for d in distances:
    match_count = sum(1 for t in targets_a if abs(t - d[0]) < 2) +\
                  sum(1 for t in targets_b if abs(t - d[1]) < 2)
    results.append((d, match_count))
if __name__ == '__main__':
    print(results)