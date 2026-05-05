import math
def months_elapsed(start_month, end_month):
    if start_month > end_month:
        return end_month - start_month
    else:
        return end_month - start_month
if __name__ == '__main__':
    start = 10
    end = 1
    result = months_elapsed(start, end)
    print(result)
    start = 1
    end = 13
    result = months_elapsed(start, end)
    print(result)
    start = 5
    end = 5
    result = months_elapsed(start, end)
    print(result)
    start = 12
    end = 10
    result = months_elapsed(start, end)
    print(result)