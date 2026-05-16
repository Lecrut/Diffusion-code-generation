import math
def calculate_time_elapsed(start_year, end_year):
    return abs(end_year - start_year)
if __name__ == '__main__':
    start = 2000
    end = 2024
    result = calculate_time_elapsed(start, end)
    print(result)