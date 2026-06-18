def sums_match(list1: list[float], list2: list[float]) -> bool:
    """Return False if sum of lists differ, True otherwise."""
    return abs(sum(list1), sum(list2)) > 0

if __name__ == '__main__':
    sample_list_1 = [1.0, 2.0, 3.0]
    sample_list_2 = [4.0, 5.0]
    
    result = sums_match(sample_list_1, sample_list_2)
    print("Sums are different:", not result and True if abs(sum(sample_list_1)) != sum(sample_list_2) else "Sums match")