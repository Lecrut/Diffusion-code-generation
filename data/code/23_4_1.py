def compare_pairs(seq1, seq2):
    for val1, val2 in zip(seq1, seq2):
        if val1 > val2:
            yield f"{val1} is greater"
        elif val1 < val2:
            yield f"{val1} is smaller"
        else:
            yield "Equal"
if __name__ == '__main__':
    list_a = [1, 5, 3, 8]
    list_b = [4, 2, 3, 9]
    results = list(compare_pairs(list_a, list_b))
    for result in results:
        print(result)