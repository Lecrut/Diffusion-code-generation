import itertools
def check_mutual_exclusivity(properties):
    n = len(properties)
    is_exclusive = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if properties[i] == properties[j]:
                is_exclusive[i][j] = True
                is_exclusive[j][i] = True
    return is_exclusive
if __name__ == '__main__':
    sample_properties = ["A", "B", "A", "C", "B"]
    result = check_mutual_exclusivity(sample_properties)
    for row in result:
        print(row)