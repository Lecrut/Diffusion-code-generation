import time
def find_differences(str1, str2):
    list1 = [int(x.strip()) for x in str1.split(',')]
    list2 = [int(x.strip()) for x in str2.split(',')]
    set1 = set(list1)
    set2 = set(list2)
    diff1_only = list(set1 - set2)
    diff2_only = list(set2 - set1)
    return diff1_only, diff2_only
if __name__ == '__main__':
    string1 = "1,5,3,7,9,2"
    string2 = "5,8,3,10,4"
    start_time = time.perf_counter()
    diff1, diff2 = find_differences(string1, string2)
    end_time = time.perf_counter()
    print(f"Differences in {string1} only: {sorted(diff1)}")
    print(f"Differences in {string2} only: {sorted(diff2)}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")