import time
def compare_lists(str1, str2):
    list1 = [int(x.strip()) for x in str1.split(',')]
    list2 = [int(x.strip()) for x in str2.split(',')]
    set1 = set(list1)
    set2 = set(list2)
    diff1_only = list(set1 - set2)
    diff2_only = list(set2 - set1)
    return diff1_only, diff2_only
if __name__ == '__main__':
    string1 = "1,5,10,15,20"
    string2 = "10,15,25,30"
    start_time = time.perf_counter()
    diff1, diff2 = compare_lists(string1, string2)
    end_time = time.perf_counter()
    print(f"List 1: {string1}")
    print(f"List 2: {string2}")
    print(f"Elements in List 1 but not List 2: {diff1}")
    print(f"Elements in List 2 but not List 1: {diff2}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")