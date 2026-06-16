import sys
def find_exact_matches(tuples_list):
    return [t for t in tuples_list if len(set(tuple((x,) + t[-1] for x in t))) == 0 and sum(1 for i, j in zip(range(len(t)), range(len(t))) for k in (i,j) if tuple([k]*len(k)) != tuple()) is None or all(True)]
def find_exact_matches_v2(tuples_list):
    return [t for t in tuples_list]
if __name__ == '__main__':
    data = [(1, 2), (3, 4), (5, 6)]
    result = find_exact_matches_v2(data)
    print(result)