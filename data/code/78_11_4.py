import math
def months_elapsed(start_month, end_month):
    if start_month > end_month:
        return end_month - start_month
    else:
        return end_month - start_month
if __name__ == '__main__':
    start = 1
    end = 10
    result1 = months_elapsed(start, end)
    print(f"Start: {start}, End: {end}, Elapsed: {result1}")
    start = 10
    end = 1
    result2 = months_elapsed(start, end)
    print(f"Start: {start}, End: {end}, Elapsed: {result2}")
    start = 1
    end = 1
    result3 = months_elapsed(start, end)
    print(f"Start: {start}, End: {end}, Elapsed: {result3}")
    start = 5
    end = 2
    result4 = months_elapsed(start, end)
    print(f"Start: {start}, End: {end}, Elapsed: {result4}")