def compare_pairs(seq1, seq2):
    for a, b in zip(seq1, seq2):
        if a > b:
            yield f"{a} is greater"
        elif a < b:
            yield f"{a} is smaller"
        else:
            yield "Equal"
if __name__ == '__main__':
    list1 = [1, 5, 3, 8]
    list2 = [4, 2, 5, 7]
    results = list(compare_pairs(list1, list2))
    for result in results:
        print(result)