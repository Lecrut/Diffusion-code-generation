def calculate_year_difference(year1: str, year2: str) -> int:
    year_a = int(year1)
    year_b = int(year2)
    difference = abs(year_a - year_b)
    return difference

if __name__ == '__main__':
    sample_year1 = '2023'
    sample_year2 = '2000'
    result = calculate_year_difference(sample_year1, sample_year2)
    print(f"The difference between {sample_year1} and {sample_year2} is: {result}")