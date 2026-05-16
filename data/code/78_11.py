import math
def months_elapsed(start_month, end_month):
    if start_month <= end_month:
        return end_month - start_month
    else:
        return end_month - start_month
if __name__ == '__main__':
    start1 = 1
    end1 = 5
    result1 = months_elapsed(start1, end1)
    print(f"Start: {start1}, End: {end1}, Elapsed: {result1}")
    start2 = 10
    end2 = 3
    result2 = months_elapsed(start2, end2)
    print(f"Start: {start2}, End: {end2}, Elapsed: {result2}")
    start3 = 12
    end3 = 12
    result3 = months_elapsed(start3, end3)
    print(f"Start: {start3}, End: {end3}, Elapsed: {result3}")
    start4 = 1
    end4 = 13
    result4 = months_elapsed(start4, end4)
    print(f"Start: {start4}, End: {end4}, Elapsed: {result4}")